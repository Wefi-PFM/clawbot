---
name: clawathon-grader
description: >-
  Chấm pass/fail bài nộp Claw-a-thon 2026 (VNG / GreenNode AI hackathon) dựa trên rulebook
  và checklist của BTC. Dùng skill này bất cứ khi nào người dùng đưa link repo GitHub của một
  đội thi (kèm link demo video / AgentBase / mô tả use case), hoặc một file export form (CSV/Excel)
  nhiều đội, và muốn rà soát bài nộp, chấm PASS/FAIL, kiểm tra README/source/demo/env.example,
  quét secret bị lộ, kiểm tra hợp lệ team name / track / thành viên, hay soạn email kết quả cho
  các đội. Trigger cả khi người dùng chỉ nói "chấm bài đội này", "review submission", "kiểm tra
  bài nộp hackathon", "soạn mail PASS/FAIL cho đội" mà không nhắc đích danh chữ "Claw-a-thon".
  KHÔNG dùng cho việc chấm điểm xếp hạng (ranking/voting) — skill này chỉ chấm vòng pass/fail (Round 1).
---

# Claw-a-thon 2026 — Chấm pass/fail bài nộp

Skill này giúp BTC rà từng bài nộp ở **vòng đánh giá nội bộ (Round 1, 17/06 13:00–17:00)** và kết luận **PASS/FAIL** theo đúng rulebook Claw-a-thon 2026 (mục 5, 6, 9, 11), rồi soạn **draft email** thông báo kết quả cho từng đội.

Triết lý chấm: **phần A là thứ quyết định pass/fail**. Phần B/C dùng để khẳng định A đạt và để phân loại lỗi thành hai nhóm — *hard-fail* (làm rớt bài) và *nhắc nhở Level 1* (đội được bổ sung). Đừng đánh rớt một bài chỉ vì lỗi Level 1. Khi nghi ngờ, ghi rõ "CẦN BTC XÁC NHẬN" thay vì tự kết luận rớt — vì hậu quả của một FAIL sai là đội bị loại oan.

## Đầu vào skill nhận

Mỗi bài nộp gồm các trường (lấy từ Submission Form):

- **Team name** (≤60 ký tự, unique)
- **Track** (1 trong 3: Agentic Assistant / Data Analysis / Automation & Integration)
- **Link repo GitHub** (public hoặc internal)
- **Link demo video** (YouTube hoặc OneDrive share trong domain VNG)
- **Cách dùng thử agent** — một trong hai: **link AgentBase** (nơi agent đang chạy), HOẶC nếu là case OpenClaw chạy qua **chat tool** thì là **link/handle bot** (Telegram, Zalo, Messenger…). Trường này trống KHÔNG đồng nghĩa FAIL — xem A1 ở Bước 1.
- **Mô tả use case trong form** (≤300 từ)
- **Thành viên**: 1–3 người, email `@vng.com.vn`, có department

Người dùng có thể đưa **một đội** (dán link + thông tin) hoặc **cả lô** (file CSV/Excel export từ Zoho Form). Nếu thiếu trường nào để chấm, hỏi lại đúng trường còn thiếu — đừng đoán.

## Quy trình chấm (làm tuần tự cho mỗi đội)

### Bước 0 — Thu thập & clone

1. Xác định đầy đủ các trường đầu vào ở trên. Với file export: đọc bằng skill `xlsx` (nếu .xlsx) hoặc đọc CSV trực tiếp, mỗi dòng = 1 đội.
2. Clone repo về sandbox để soi file thật (đừng chấm "chay" từ trí nhớ):
   ```bash
   git clone --depth 1 <repo_url> /tmp/grade/<team_slug> 2>&1 | tail -5
   ```
   Nếu clone lỗi (repo private/không tồn tại/sai link) → đây là tín hiệu cho **B2** ("repo không mở được / sai link trong form"), ghi lại nguyên văn lỗi. Lưu ý: repo internal/private có thể là hợp lệ (rulebook cho phép internal) — BTC cần kiểm quyền truy cập; đừng auto-FAIL chỉ vì người ngoài không clone được.
3. Đọc cây thư mục: `find /tmp/grade/<team_slug> -not -path '*/.git/*' | head -100` để biết có `README.md`, `demo/`, `env.example`, source code không.

### Bước 1 — Kiểm tra link (A1, A2)

Quan trọng phải hiểu đúng giới hạn: **status code không chứng minh được "agent trả lời được" hay "video đúng track"**, và môi trường chấm thường chỉ có mạng allowlist nên link nội bộ VNG (vngcloud, sharepoint) hay trả về `000` — đây là *"không kiểm tra được từ đây"*, **không phải link chết**. Vì vậy skill chỉ làm phần lọc sơ bộ tự động được, còn xác nhận cuối cùng giao cho người mở link.

Chạy script kiểm link (vừa kiểm định dạng offline, vừa probe HTTP best-effort):

```bash
python3 <skill_dir>/scripts/check_links.py \
  --agentbase "<agentbase_url>" --video "<video_url>" --repo "<repo_url>"
```

Script trả JSON cho từng link với `format` (định dạng có đúng loại không) và `probe_state`. Diễn giải:
- `format: suspect` → **link điền nhầm** (vd link AgentBase lại là youtube.com) → cờ đỏ, ghi rõ để BTC kiểm.
- `probe_state: dead` (HTTP 404) → gần như chắc chắn link chết → cờ đỏ A1/A2.
- `probe_state: unreachable_here` (000) hoặc `needs_login` (401/403) → **MANUAL**, KHÔNG kết luận FAIL. Đây là trường hợp phổ biến nhất với link VNG.
- `probe_state: reachable` (200/3xx) → link sống về mặt mạng, nhưng **vẫn MANUAL** để xác nhận nội dung.

**Nếu KHÔNG có link AgentBase:** đừng vội FAIL. Kiểm xem có phải case **OpenClaw chạy qua chat tool** không — tìm trong form/README/video dấu hiệu Telegram/Zalo/Messenger (link mời bot, handle `@...bot`, hướng dẫn "nhắn cho bot trên Zalo/Telegram"). Nếu có → A1 chuyển sang xác minh qua kênh chat (xem checklist dưới). Chỉ FAIL A1 khi **không có bất kỳ** cách dùng thử nào: không URL, không kênh chat, và video cũng không thể hiện agent chạy.

**Checklist MANUAL cho người chấm (dùng trình duyệt/ứng dụng nào cũng được — Edge, Chrome, Telegram, Zalo… miễn đã đăng nhập tài khoản VNG khi cần):**

- **A1 — agent active (qua AgentBase):** mở link AgentBase → giao diện chat hiện ra → **gõ 1 câu hỏi test đúng use case** (vd agent tìm vé: "Tìm vé Hà Nội đi Đà Nẵng ngày 20/7") → agent **trả lời được** (không lỗi 500/treo/timeout). Trả lời được = A1 đạt.
- **A1 — agent active (qua chat tool):** mở bot trên Telegram/Zalo theo link/handle đội cung cấp → **nhắn 1 câu test** → bot trả lời = A1 đạt. Nếu không nhắn trực tiếp được, xem demo video có thể hiện agent chạy end-to-end qua chat tool không. Đạt một trong hai = A1 đạt.
- A1 chỉ **FAIL** khi không mở/không nhắn được VÀ video cũng không chứng minh agent hoạt động.
- **A2 — video hợp lệ:** mở link video bằng tài khoản VNG → **bấm play, xem 2–3 phút đầu** → đúng track đã đăng ký, demo end-to-end 1 use case thật. Video **dài hơn 3 phút KHÔNG rớt** (chỉ xem 3 phút đầu). Chỉ rớt A2 khi link chết, không xem được, hoặc demo **sai track**.

Ghi kết quả A1/A2 vào bảng chấm là ⚠️ MANUAL kèm hướng dẫn trên. Skill không tự đánh PASS/FAIL cho A1/A2 trừ khi có bằng chứng rõ ràng (`suspect` / `dead`, hoặc hoàn toàn không có cách dùng thử).

### Bước 2 — Chấm checklist A / B / C

Đọc đầy đủ tiêu chí, cách phân loại lỗi, và mọi trích dẫn rulebook trong:

→ **`references/grading-criteria.md`** (đọc file này trước khi chấm — nó là nguồn chân lý cho từng mục tick)

Tóm tắt mức cao:
- **A1, A2, A3**: rớt 1 trong 3 = **FAIL cả bài** (rulebook mục 6). Lưu ý A1 có 2 hình thức hợp lệ (AgentBase URL hoặc chat tool) — xem grading-criteria.
- **B (4 deliverable)**: README / source / demo/ / env.example. Phần lớn lỗi B là **Level 1 nhắc nhở** (đội bổ sung được), TRỪ: README/form trống-placeholder (đụng A3 → FAIL) và **env.example chứa secret thật** (xem Bước 3).
- **C (hợp lệ & tuân thủ)**: phần lớn là điều kiện loại (disqualify Level 2/3) nếu vi phạm nặng — sai track, trùng người ở nhiều đội, dùng PII/dữ liệu khách hàng thật, không khai báo AI với người dùng cuối, copy agent đội khác, vi phạm content policy 11.1.

### Bước 3 — Quét secret bị lộ (bắt buộc)

Đây là mục dễ bỏ sót và rủi ro bảo mật cao (rulebook mục 4 cấm chia sẻ token). `env.example` chỉ được chứa **placeholder**, không được có token/secret thật. Chạy script quét toàn repo:

```bash
python3 <skill_dir>/scripts/scan_secrets.py /tmp/grade/<team_slug>
```

Diễn giải output (script in JSON: `findings[]` với file, dòng, loại, snippet đã che):
- Phát hiện **token/secret thật** (`high`) → **cờ bảo mật**: ghi rõ file + dòng (che bớt giá trị), khuyến nghị BTC liên hệ đội xoay token ngay. Theo rulebook mục 4 + 11.3 đây có thể là Level 2/3 tuỳ mức độ — KHÔNG tự quyết mức phạt, nêu phát hiện + đề xuất để BTC quyết.
- Chỉ có placeholder / biến môi trường (`CLEAN` hoặc chỉ `low`) → đạt yêu cầu env.example. Mục `low` (vd `self.token = token`) thường lành tính — liếc qua ngữ cảnh nếu cần.

Script tự bỏ qua `.git/`, nhận diện placeholder và biểu thức code (`${VAR}`, `os.environ...`) để giảm báo nhầm. Nếu script báo nghi ngờ ở vùng xám, mở file xem ngữ cảnh rồi mới kết luận.

### Bước 4 — Phân loại lỗi & kết luận

Gom mọi phát hiện vào hai rổ (chi tiết trong `references/grading-criteria.md`):

- **HARD-FAIL** → bài FAIL: thiếu bất kỳ A1/A2/A3; sai track; (theo rulebook 1.2) không có thành viên dự Training 10/06 nếu BTC nắm thông tin này; dùng PII/dữ liệu thật; vi phạm content policy nặng; lộ secret thật mức nghiêm trọng; trùng người ở nhiều đội.
- **LEVEL 1 — nhắc nhở (vẫn PASS, đội bổ sung được)**: thiếu attribution sample/open source; README sơ sài nhưng vẫn có problem/user/solution; thiếu 1 screenshot; thiếu khai báo model ngoài MaaS trong README.

Kết luận theo rulebook mục 6:
- **PASS** ⇔ A1 **và** A2 **và** A3 đều đạt **VÀ** không dính vi phạm phần C ở mức disqualify (Level 2/3).
- **FAIL** ⇔ thiếu bất kỳ tiêu chí A nào, hoặc dính vi phạm nặng.

Đội FAIL được **appeal/bổ sung 1 lần duy nhất** trong 18–19/06 → luôn nêu rõ điều này trong email FAIL.

### Bước 5 — Xuất kết quả

**Nơi lưu:** tất cả file kết quả lưu vào thư mục `output/` ngay trong thư mục skill (tạo nếu chưa có). Nếu skill được cài ở vị trí chỉ-đọc nên không ghi được vào `output/`, đổi sang folder làm việc của người dùng và báo rõ đường dẫn. Mỗi lần chấm lô nên gom vào subfolder theo ngày, vd `output/2026-06-17/`, để khỏi lẫn các đợt.

**Quy mô mỗi lần chạy:** khuyến nghị **10–15 đội mỗi file/đợt** (tối đa ~20). Mỗi đội tốn clone + quét + check link + suy luận nên lô quá lớn dễ chậm và sót; nếu danh sách dài hơn, chia thành nhiều đợt (theo BTC PIC hoặc theo track).

Quy tắc số lượng file draft email (làm đúng theo đây):

**Chấm 1 đội** → xuất đúng **1 file markdown draft email**: `output/<team_slug>_email.md`. Chọn template PASS (mời vào vòng voting VNG Group) hoặc FAIL (lý do cụ thể từng mục + hướng dẫn appeal 18–19/06) từ `references/email-templates.md`. Kèm theo **1 file bảng chấm chi tiết** `output/<team_slug>_grading.md` (từng mục A/B/C đã tick ✅/❌/⚠️MANUAL, danh sách phát hiện, kết luận PASS/FAIL).

**Chấm nhiều đội (cả lô)** → KHÔNG rải mỗi đội một file email lẻ. Thay vào đó gộp **tất cả** vào **đúng 1 file markdown** `output/all_draft_emails.md`, mỗi đội là một section riêng (dùng `## <Team name> — PASS/FAIL` làm tiêu đề, ngăn cách bằng `---`) để BTC cuộn xuống copy từng email. Kèm thêm **1 file bảng tổng hợp** `output/summary.md` (1 hàng/đội: PASS/FAIL, A1/A2/A3, số lỗi Level 1, cờ bảo mật). Bảng chấm chi tiết từng đội là tuỳ chọn khi lô lớn — nếu người dùng cần, vẫn xuất `output/<team_slug>_grading.md` cho từng đội. Nếu người dùng muốn bảng tổng hợp dạng Excel, dùng skill `xlsx`.

Sau khi tạo file, dùng `present_files` để người dùng mở. Trình bày ngắn gọn: bao nhiêu đội PASS/FAIL, đội nào có cờ bảo mật cần xử lý gấp.

## Nguyên tắc khi diễn giải (quan trọng)

- **Không tự quyết mức phạt Level 2/3.** Skill phát hiện và đề xuất; BTC là người quyết loại đội. Với mọi nghi ngờ nặng (PII, copy agent, content policy), ghi "ĐỀ XUẤT BTC RÀ SOÁT" kèm bằng chứng (file/dòng/đoạn text).
- **Phân biệt "không kiểm tra được" với "FAIL".** Repo internal cần login, OneDrive trong domain VNG, link VNG trả 000, hay agent chạy qua chat tool — đây là MANUAL, không phải FAIL. Chỉ FAIL khi có bằng chứng rõ ràng (link 404, README trống, sai track, hoàn toàn không có cách dùng thử agent).
- **Trích dẫn rulebook** trong mỗi lý do FAIL/Level 1 (vd "mục 6 — A2", "mục 11.2 — attribution") để email có căn cứ và đội đỡ thắc mắc.
- **Che secret** khi báo cáo: chỉ hiện 4 ký tự đầu + `***`, không in nguyên token ra file/email.

## Tài nguyên đi kèm

- `references/grading-criteria.md` — checklist A/B/C/D đầy đủ, mapping rulebook, cách phân loại hard-fail vs Level 1. **Đọc trước khi chấm.**
- `references/email-templates.md` — template email PASS và FAIL (song ngữ VN/EN), có chỗ điền lý do.
- `scripts/scan_secrets.py` — quét token/secret thật trong repo, nhận diện placeholder/biến env để giảm báo nhầm.
- `scripts/check_links.py` — kiểm sơ bộ link AgentBase/video/repo (đúng định dạng + probe HTTP), không phụ thuộc trình duyệt; xác nhận cuối vẫn do người mở link.
