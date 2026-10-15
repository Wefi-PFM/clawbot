#!/usr/bin/env python3
"""
scan_secrets.py - Quet token/secret that trong repo bai nop Claw-a-thon.

Phan biet SECRET THAT voi PLACEHOLDER hop le va BIEU THUC CODE (env.example chi
duoc chua placeholder, muc 4 rulebook). Giam bao nham bang allowlist placeholder
+ nhan dien tham chieu bien moi truong / bieu thuc code.

Cach dung: python3 scan_secrets.py <duong_dan_repo>
In JSON. Moi finding: {file, line, type, severity, snippet (da che)}.
"""
import argparse
import json
import os
import re
import sys

PATTERNS = [
    ("openai_key",        re.compile(r"sk-[A-Za-z0-9]{20,}"),                       "high"),
    ("anthropic_key",     re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}"),               "high"),
    ("aws_access_key",    re.compile(r"AKIA[0-9A-Z]{16}"),                          "high"),
    ("google_api_key",    re.compile(r"AIza[0-9A-Za-z_\-]{35}"),                    "high"),
    ("github_token",      re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),               "high"),
    ("slack_token",       re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"),            "high"),
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----"), "high"),
    ("jwt",               re.compile(r"eyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"), "medium"),
]

KV_NAME = re.compile(
    r"(?i)\b([A-Z0-9_]*(?:TOKEN|SECRET|API[_-]?KEY|PASSWORD|PASSWD|PRIVATE[_-]?KEY|ACCESS[_-]?KEY|CLIENT[_-]?SECRET)[A-Z0-9_]*)\b"
    r"\s*[:=]\s*"
    r"['\"]?([^\s'\"#]+)"
)

PLACEHOLDER_HINTS = [
    "your", "xxx", "changeme", "change_me", "example", "placeholder", "dummy",
    "todo", "fill", "here", "replace", "insert", "<", ">", "...", "***",
    "abcdef", "123456", "token_here", "value_here", "my_", "sample", "test",
    "none", "null", "n/a", "na", "empty", "secret_key", "your-token", "xxxx",
]
PLACEHOLDER_EXACT = {"", "true", "false", "0", "1", "localhost", "127.0.0.1"}

CODE_REF_SUBSTR = (
    "${", "os.environ", "os.getenv", "getenv", "process.env", "import.meta.env",
    "request.", "req.", "self.", "raw.", "headers", ".get(", "config.", "settings.",
    "<%", "{{", "}}", "lambda", "=>",
)

SKIP_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico", ".pdf",
    ".zip", ".tar", ".gz", ".mp4", ".mov", ".mp3", ".woff", ".woff2",
    ".ttf", ".eot", ".lock", ".map", ".bin", ".so", ".pyc", ".ds_store",
}
SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build", ".next"}

MAX_FILE_BYTES = 5000000


def is_placeholder(value):
    v = value.strip().strip("'\"").lower()
    if v in PLACEHOLDER_EXACT:
        return True
    if len(v) < 8:
        return True
    if any(h in v for h in PLACEHOLDER_HINTS):
        return True
    if len(set(v)) <= 2:
        return True
    return False


def is_code_reference(value):
    v = value.strip().strip("'\"").rstrip(",);")
    if not v:
        return False
    low = v.lower()
    if any(s in low for s in CODE_REF_SUBSTR):
        return True
    if any(c in v for c in "()[]+"):
        return True
    if re.fullmatch(r"[A-Z][A-Z0-9_]{2,}", v):
        return True
    return False


def redact(value):
    value = value.strip().strip("'\"")
    if len(value) <= 4:
        return "***"
    return value[:4] + "***(" + str(len(value)) + " chars)"


def looks_like_real_secret(value):
    v = value.strip().strip("'\"")
    if is_placeholder(v) or is_code_reference(v):
        return False
    if len(v) < 16:
        return False
    classes = sum([
        bool(re.search(r"[a-z]", v)),
        bool(re.search(r"[A-Z]", v)),
        bool(re.search(r"[0-9]", v)),
        bool(re.search(r"[^A-Za-z0-9]", v)),
    ])
    return classes >= 2


def scan_file(path, rel, max_bytes):
    findings = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read(max_bytes)
    except Exception:
        return findings
    for i, line in enumerate(data.splitlines(), 1):
        if len(line) > 4000:
            continue
        for name, pat, sev in PATTERNS:
            m = pat.search(line)
            if m:
                findings.append({"file": rel, "line": i, "type": name,
                                 "severity": sev, "snippet": redact(m.group(0))})
        for m in KV_NAME.finditer(line):
            var, val = m.group(1), m.group(2)
            if is_placeholder(val) or is_code_reference(val):
                continue
            sev = "high" if looks_like_real_secret(val) else "low"
            findings.append({"file": rel, "line": i, "type": "assigned_secret:" + var,
                             "severity": sev, "snippet": var + "=" + redact(val)})
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--max-bytes", type=int, default=1000000)
    args = ap.parse_args()

    if not os.path.isdir(args.repo):
        print(json.dumps({"error": "not a directory: " + args.repo}))
        sys.exit(0)

    all_findings = []
    for root, dirs, files in os.walk(args.repo):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if any(fn.lower().endswith(e) for e in SKIP_EXT):
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, args.repo)
            try:
                if os.path.getsize(full) > MAX_FILE_BYTES:
                    continue
            except OSError:
                continue
            all_findings.extend(scan_file(full, rel, args.max_bytes))

    high = [f for f in all_findings if f["severity"] == "high"]
    medium = [f for f in all_findings if f["severity"] == "medium"]
    low = [f for f in all_findings if f["severity"] == "low"]
    verdict = ("LEAKED_SECRET_LIKELY" if high else
               "REVIEW_NEEDED" if medium else
               "LOW_RISK_REVIEW" if low else "CLEAN")
    result = {
        "repo": args.repo,
        "summary": {"high": len(high), "medium": len(medium), "low": len(low), "verdict": verdict},
        "note": ("high=gan nhu chac chan secret that (co bao mat, muc 4). "
                 "medium/low=can nguoi xem ngu canh. CLEAN=chi placeholder/bien env hoac khong co gi."),
        "findings": high + medium + low,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
