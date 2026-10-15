# Checklist chấm Claw-a-thon 2026 (đầy đủ)

Nguồn: Rulebook Claw-a-thon 2026 v1.2 (mục 5 Submission Format, mục 6 Pass/Fail, mục 9 IP, mục 11 Ethics) + 4 deliverable trong sample package. Chấm theo **trạng thái repo tại 12:00 ngày 17/06** (form đóng); mọi commit/deploy sau mốc này không tính (mục 5.2).

Ký hiệu khi tick: ✅ đạt · ❌ không đạt · ⚠️ MANUAL (cần BTC xác nhận bằng mắt) · 🔒 cờ bảo mật.

---

## A. ĐIỀU KIỆN PASS BẮT BUỘC (mục 6 — rớt 1 = FAIL cả bài)

Ba điều kiện phải **đồng thời** thỏa.

### A1. Agent đang chạy & gọi thử được
Ý nghĩa cốt lõi: **BTC có cách dùng thử agent và agent phản hồi được**. Có **hai hình thức hợp lệ** — không bắt buộc phải có URL AgentBase:
- **(a) Có link AgentBase đang chạy** → BTC mở link, gọi thử ≥1 request thành công.
- **(b) Agent chạy qua chat tool (OpenClaw + Telegram / Zalo / Messenger…)** → KHÔNG cần URL AgentBase. A1 đạt nếu BTC kiểm chứng được agent đang hoạt động qua kênh chat đó: có link/handle bot để nhắn thử (vd link Telegram bot, Zalo OA/bot), HOẶC demo video thể hiện rõ agent chạy end-to-end qua chat tool.
- **PASS**: thoả (a) hoặc (b).
- **FAIL**: không có **bất kỳ** cách nào để dùng thử (không URL, không kênh chat, không demo thuyết phục), hoặc agent gọi vào báo lỗi/không phản hồi.
- **Quan trọng — KHÔNG auto-FAIL chỉ vì thiếu URL AgentBase.** Nếu trường "Link dùng thử Agent" trống, kiểm tra form/README/video xem có phải case chat tool (b) không trước khi kết luận.
- **Skill làm gì**: nếu có URL → `check_links.py` (404 = cờ đỏ; 000/401/403 = ⚠️ MANUAL "BTC thử gọi 1 request"). Nếu KHÔNG có URL → tìm dấu hiệu chat tool (link/handle Telegram/Zalo trong form hoặc README, mô tả "chạy qua Zalo/Telegram") → ghi ⚠️ MANUAL "BTC kiểm chứng agent qua kênh chat / qua video", KHÔNG tự FAIL.

### A2. Demo video hợp lệ
- PASS: video 2–3 phút, mở được bằng tài khoản VNG (YouTube hoặc OneDrive share trong domain VNG), thể hiện agent chạy **đúng track đã đăng ký**, end-to-end cho 1 use case thực tế.
- FAIL: video chết link, không xem được, hoặc demo **sai track**.
- Lưu ý: video **>3 phút KHÔNG rớt** (BTC chỉ xem 3 phút đầu — FAQ).
- **Skill làm gì**: thử resolve link (`check_links.py`). Nội dung (đúng track, đúng thời lượng, end-to-end) = ⚠️ MANUAL. Video để trên Google Drive / domain không phải VNG → ghi cờ "kiểm kênh video" (mục 5.1 yêu cầu YouTube hoặc OneDrive/SharePoint VNG).

### A3. Mô tả use case đầy đủ
- PASS: có **cả** README trong repo **và** mô tả trong form (≤300 từ), nêu rõ **problem, user, solution (+ value)**.
- FAIL: để trống / placeholder / lorem ipsum / copy template chưa sửa.
- **Skill làm gì**: đọc README + mô tả form, kiểm tra có đủ 3 ý và không phải text mẫu chưa sửa. Đây là phần B1 dùng để khẳng định A3.

---

## B. CHECKLIST DELIVERABLE (4 mục)

Phần lớn lỗi B = **Level 1 nhắc nhở** (đội bổ sung được, vẫn PASS), TRỪ các mục đụng A3 hoặc secret thật (ghi rõ bên dưới).

### B1. README.md
- [ ] Có mục **Problem** (bài toán giải quyết) — *thiếu nội dung thật → đụng A3 → FAIL*
- [ ] Có mục **Users** (ai dùng) — *thiếu → đụng A3*
- [ ] Có mục **Solution** (agent giải quyết ra sao + giá trị) — *thiếu → đụng A3*
- [ ] Có mục **How to run** (chạy lại được, không mơ hồ) — *thiếu/mơ hồ → Level 1*
- [ ] Có mục **What to customize** (chỗ người khác chỉnh được) — *thiếu → Level 1*
- [ ] Viết rõ ràng, người ngoài đọc hiểu, **không phải template gốc chưa sửa** — *còn nguyên template → đụng A3 → FAIL*
- [ ] Nếu dùng **model ngoài MaaS** (OpenAI, Anthropic…) phải **khai báo rõ trong README** (FAQ) — *thiếu khai báo → Level 1*

Cách nhận biết "template chưa sửa": còn chữ như "Your problem here", "[Mô tả use case]", "TODO", "lorem ipsum", hoặc trùng y hệt README mẫu trong sample package.

### B2. Source code
- [ ] Repo (GitHub public hoặc internal) **mở được**, đúng link trong form — *clone lỗi/sai link → ghi nhận; repo internal/private có thể hợp lệ, BTC kiểm quyền truy cập; nếu hoàn toàn không có repo nào → cân nhắc FAIL*
- [ ] Code **khớp với agent đang chạy** — *⚠️ MANUAL (BTC đối chiếu); chỉ nghi ngờ khi repo rỗng/không liên quan*
- [ ] Có **ghi nguồn rõ ràng** nếu dùng sample template / open source (mục 11.2) — *thiếu attribution → Level 1 nhắc nhở*
- Lưu ý: link "repo" trỏ vào Google Drive / folder chia sẻ → không phải repository git → ghi cờ "cần repo git hợp lệ".

### B3. demo/
- [ ] Có **link video** (trùng/khớp với video nộp ở form) — *thiếu → Level 1 (đã có video ở form thì nhẹ)*
- [ ] Có **2–3 screenshot** — *thiếu/ít hơn → Level 1*
- [ ] Ảnh **xem được, đúng nội dung agent** (không phải placeholder) — *ảnh placeholder → Level 1*

### B4. env.example
- [ ] Liệt kê **đủ env vars** cần thiết: `MAAS_TOKEN`, `OPENCLAW_ID`, … (đủ để chạy theo "How to run") — *thiếu biến → Level 1*
- [ ] **KHÔNG chứa token/secret thật** — chỉ placeholder. *Lộ token thật → 🔒 cờ bảo mật (mục 4 cấm chia sẻ token), nặng có thể Level 2/3 → BTC quyết*

---

## C. KIỂM TRA HỢP LỆ & TUÂN THỦ (mục 5.1, 9, 11)

Phần lớn vi phạm nặng ở C = **disqualify (Level 2/3)** → kéo bài xuống FAIL. Skill **phát hiện + đề xuất**, BTC quyết mức phạt.

- [ ] **Team name** unique, ≤60 ký tự, không trùng đội khác — *trùng → ưu tiên đội đăng ký sớm hơn (mục 5.1); >60 ký tự → Level 1 nhắc sửa. Đối chiếu trùng tên cần danh sách tất cả đội → ⚠️ MANUAL nếu chỉ chấm 1 bài.*
- [ ] **Track**: đúng 1 trong 3, và **khớp với agent demo** — *demo sai track → FAIL (đụng A2). Tên track không khớp 3 lựa chọn chính thức (vd "Chat Agent") → ⚠️ làm rõ, ánh xạ gần nhất là Agentic Assistant.*
- [ ] **Thành viên**: 1–3 người, email `@vng.com.vn`, có ghi department — *sai định dạng/thiếu department → Level 1; >3 người → vi phạm (FAQ: max 3)*
- [ ] **Mỗi cá nhân chỉ thuộc 1 đội / 1 bài nộp** — *trùng người ở nhiều đội → disqualify (mục 1.2). Cần danh sách toàn cuộc → ⚠️ MANUAL nếu chấm lẻ.*
- [ ] **Agent khai báo rõ là AI** với người dùng cuối (mục 11.1, bắt buộc — cấm giả người thật) — *không khai báo/giả người → vi phạm 11.1 → ĐỀ XUẤT BTC rà soát*
- [ ] **Không dùng dữ liệu khách hàng thật / PII / nội bộ confidential** (mục 9.2 — chỉ public/synthetic/anonymized) — *dùng PII/dữ liệu thật → HARD-FAIL/disqualify*
- [ ] **Không copy agent đội khác** (mục 11.2) — *nghi copy → ĐỀ XUẤT BTC rà soát*
- [ ] **Nội dung agent không vi phạm content policy** mục 11.1 (a–k: bôi nhọ, phân biệt đối xử, khiêu dâm/bạo lực, lừa đảo, vi phạm IP…) — *vi phạm → disqualify*

Thông tin training (mục 1.2: ≥1 thành viên dự Training 10/06) và đối chiếu trùng tên/trùng người thường nằm ngoài repo → đánh dấu ⚠️ MANUAL để BTC kiểm tra từ hồ sơ đăng ký.

---

## D. KẾT LUẬN CHẤM

- **PASS** ⇔ A1 + A2 + A3 đều đạt **VÀ** không vi phạm phần C ở mức disqualify (Level 2/3).
- **FAIL** ⇔ thiếu bất kỳ tiêu chí A nào, **hoặc** dính vi phạm nặng (PII, copy, content policy, sai track, lộ secret nghiêm trọng…).
- **PENDING** (khi cần): nếu chưa đủ thông tin để xác minh A (vd không có cách dùng thử agent, repo chưa truy cập được) nhưng chưa có bằng chứng FAIL rõ ràng → để PENDING và yêu cầu đội bổ sung trong 18–19/06, thay vì FAIL oan.

### Phân loại lỗi (rất quan trọng — đừng đánh rớt vì lỗi nhẹ)

| Nhóm | Hậu quả | Ví dụ |
|---|---|---|
| **HARD-FAIL** | Bài FAIL | Thiếu A1/A2/A3; sai track; dùng PII/dữ liệu thật; vi phạm content policy 11.1; lộ secret thật nghiêm trọng; trùng người ở nhiều đội; (nếu BTC nắm) không có thành viên dự Training 10/06 |
| **LEVEL 1 — nhắc nhở** | Vẫn PASS, đội bổ sung được | Thiếu attribution; README có đủ problem/user/solution nhưng sơ sài; thiếu mục How to run / What to customize; thiếu 1 screenshot; thiếu khai báo model ngoài MaaS; team name >60 ký tự; thiếu department |

Lưu ý: **2 lỗi Level 1 có thể thành Level 2** (mục 11.3) → nếu một đội dính nhiều Level 1, ghi chú để BTC cân nhắc.

### Sau khi FAIL
Gửi email nêu lý do cụ thể **ngay trong ngày 17/06**. Đội được **appeal/bổ sung 1 lần duy nhất** trong **18–19/06** (mục 6 + timeline). Luôn nêu rõ quyền này trong email FAIL.
