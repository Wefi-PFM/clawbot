#!/usr/bin/env python3
"""
check_links.py - Kiem tra so bo cac link trong bai nop Claw-a-thon.

Lam 2 viec, deu KHONG phu thuoc trinh duyet nao:
  1) Kiem dinh dang / dung loai link (offline, luon chay duoc): bat loi dien nham
     (vd link AgentBase lai la youtube.com), link sai domain video, v.v.
  2) Probe HTTP status (best-effort): chi de phat hien link 404 ro rang.
     LUU Y: moi truong chay thuong chi co mang allowlist -> link VNG noi bo
     (vngcloud, sharepoint) hay tra ve 000 = KHONG ket luan duoc tu day -> MANUAL.

Ket luan cuoi cung (agent goi duoc / video dung track) LUON can nguoi mo bang
trinh duyet da dang nhap VNG. Script chi loc bot va chi ra link kha nghi.

Cach dung:
  python3 check_links.py --agentbase <url> --video <url> --repo <url>
(bo qua tham so nao khong co)
"""
import argparse
import json
import re
import subprocess
import urllib.parse

# Domain coi la "khong phai endpoint agent" -> neu link AgentBase tro vao day la nghi dien nham
NOT_AGENT_HOSTS = ("youtube.com", "youtu.be", "google.com", "drive.google.com",
                   "docs.google.com", "facebook.com", "github.com", "sharepoint.com",
                   "onedrive.live.com")
VIDEO_OK_HINTS = ("youtube.com", "youtu.be", "sharepoint.com", "onedrive", "-my.sharepoint")
AGENT_OK_HINTS = ("agentbase", "aiplatform", "vngcloud", "endpoint-")


def host_of(url):
    try:
        return (urllib.parse.urlparse(url).hostname or "").lower()
    except Exception:
        return ""


def probe(url):
    """Tra ve HTTP status code dang chuoi; '000' = khong ket noi duoc tu day."""
    try:
        out = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
             "-L", "--max-time", "15", url],
            capture_output=True, text=True, timeout=20,
        )
        return out.stdout.strip() or "000"
    except Exception:
        return "000"


def interpret(status):
    if status in ("200", "201", "204") or status.startswith("3"):
        return "reachable", "Link phan hoi OK (van can mo that de xac nhan noi dung)."
    if status in ("401", "403"):
        return "needs_login", "Link yeu cau dang nhap (co the noi bo VNG) -> MANUAL."
    if status == "404":
        return "dead", "HTTP 404 -> link gan nhu chac chan chet (co do)."
    if status == "000":
        return "unreachable_here", "Khong ket noi duoc tu moi truong nay (mang allowlist / can VNG) -> MANUAL, KHONG ket luan chet."
    return "other", "HTTP " + status + " -> can nguoi xem."


def check(kind, url):
    h = host_of(url)
    r = {"kind": kind, "url": url, "host": h, "format": "ok", "format_note": "", "needs_manual": True}
    if not url or not h:
        r["format"] = "missing_or_invalid"
        r["format_note"] = "Thieu link hoac URL khong hop le."
        return r

    if kind == "agentbase":
        if any(b in h for b in NOT_AGENT_HOSTS) and not any(a in h for a in AGENT_OK_HINTS):
            r["format"] = "suspect"
            r["format_note"] = "Host '" + h + "' khong giong endpoint AgentBase -> nghi dien nham link."
        elif not any(a in h for a in AGENT_OK_HINTS):
            r["format"] = "warn"
            r["format_note"] = "Host khong chua dau hieu AgentBase (agentbase/aiplatform/vngcloud) -> BTC xac nhan."
    elif kind == "video":
        if not any(a in h for a in VIDEO_OK_HINTS):
            r["format"] = "warn"
            r["format_note"] = "Host '" + h + "' khong phai YouTube/OneDrive/SharePoint VNG -> kiem tra lai."
    elif kind == "repo":
        if "github.com" not in h and "git" not in h:
            r["format"] = "warn"
            r["format_note"] = "Host '" + h + "' khong giong repo git -> kiem tra lai."

    status = probe(url)
    state, note = interpret(status)
    r["http_status"] = status
    r["probe_state"] = state
    r["probe_note"] = note
    r["needs_manual"] = state not in ("dead",)  # 'dead' co the ket luan ngay; con lai can nguoi
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agentbase")
    ap.add_argument("--video")
    ap.add_argument("--repo")
    args = ap.parse_args()
    results = []
    if args.agentbase:
        results.append(check("agentbase", args.agentbase))
    if args.video:
        results.append(check("video", args.video))
    if args.repo:
        results.append(check("repo", args.repo))
    print(json.dumps({
        "results": results,
        "reminder": ("Xac nhan cuoi cung A1 (agent tra loi) va A2 (video dung track) "
                     "LUON can nguoi mo link bang trinh duyet da dang nhap VNG - dung "
                     "trinh duyet nao cung duoc (Edge/Chrome/...). Script chi loc so bo."),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
