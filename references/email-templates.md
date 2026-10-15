# Email templates — kết quả Round 1

Quy ước: thay phần `{trong ngoặc}`. Giữ giọng văn lịch sự, rõ ràng, có căn cứ rulebook. Người gửi: BTC Claw-a-thon 2026 (`info@greennode.vn`). Gửi cho team leader (representative). **Không in token/secret thật vào email** — chỉ mô tả "phát hiện secret ở file X".

Mỗi đội xuất 1 email. Mặc định viết tiếng Việt; nếu đội nộp bằng tiếng Anh hoặc người dùng yêu cầu, dùng bản EN bên dưới.

---

## 1. PASS — mời vào vòng voting (VN)

> **Tiêu đề:** [Claw-a-thon 2026] Kết quả vòng đánh giá — Đội {Team name}: PASS ✅
>
> Chào team **{Team name}**,
>
> Cảm ơn các bạn đã hoàn thành Claw-a-thon 2026. Sau vòng đánh giá nội bộ (Round 1), bài nộp của đội **ĐẠT (PASS)** và đủ điều kiện vào **vòng bình chọn cộng đồng VNG Group**.
>
> Tóm tắt kiểm tra:
> - Agent chạy trên AgentBase: {kết quả}
> - Demo video hợp lệ (2–3 phút, đúng track {Track}): {kết quả}
> - Mô tả use case (README + form): đầy đủ problem / user / solution
>
> {NẾU CÓ lỗi Level 1 — nhắc nhở, không ảnh hưởng PASS: liệt kê ngắn, vd "Lưu ý nhỏ: README chưa ghi nguồn template tham khảo (mục 11.2) — đội nên bổ sung trước khi trang voting public."}
>
> Các mốc tiếp theo: danh sách bài hợp lệ công bố **22/06**; bình chọn **22/06–03/07**; trao giải **03/07**. Mọi commit/deploy sau 12:00 ngày 17/06 sẽ không được tính cho bài đã PASS (mục 5.2).
>
> Chúc đội may mắn ở vòng bình chọn!
> — BTC Claw-a-thon 2026

---

## 2. FAIL — nêu lý do + hướng dẫn appeal (VN)

> **Tiêu đề:** [Claw-a-thon 2026] Kết quả vòng đánh giá — Đội {Team name}: CHƯA ĐẠT (cần bổ sung)
>
> Chào team **{Team name}**,
>
> Cảm ơn các bạn đã tham gia Claw-a-thon 2026. Sau vòng đánh giá nội bộ (Round 1), bài nộp của đội **CHƯA ĐẠT (FAIL)** vì (các) lý do sau:
>
> {Liệt kê từng lý do hard-fail, mỗi dòng kèm trích dẫn rulebook. Ví dụ:
> - **A1 (mục 6):** BTC không truy cập được link AgentBase {link} (HTTP 404) — agent chưa ở trạng thái chạy.
> - **A2 (mục 6):** Video demo {link} không mở được bằng tài khoản VNG / demo sai track đã đăng ký ({Track}).
> - **A3 (mục 6):** README còn ở dạng template chưa chỉnh (còn chữ "Your problem here"), chưa nêu rõ problem/user/solution.
> - **Bảo mật (mục 4):** Phát hiện token thật trong file {file} — vui lòng xoay token ngay và thay bằng placeholder.}
>
> {NẾU có lỗi Level 1 kèm theo, nêu thêm để đội sửa luôn.}
>
> **Quyền bổ sung:** Theo mục 6 của rulebook, đội được **appeal hoặc bổ sung MỘT (01) lần duy nhất** trong **18/06–19/06**. Vui lòng cập nhật và phản hồi qua kênh chính thức của BTC trước hết ngày 19/06. Kết quả pass/fail cuối cùng công bố **22/06**.
>
> Nếu cần hỗ trợ kỹ thuật (account, AgentBase, deploy), liên hệ kênh Teams của cuộc thi (KimNH/VuND3).
>
> — BTC Claw-a-thon 2026

---

## 3. PASS — invite to voting (EN)

> **Subject:** [Claw-a-thon 2026] Assessment result — Team {Team name}: PASS ✅
>
> Hi team **{Team name}**,
>
> Thank you for completing Claw-a-thon 2026. After the internal assessment (Round 1), your submission **PASSED** and qualifies for the **VNG Group community voting round**.
>
> Check summary:
> - Agent running on AgentBase: {result}
> - Valid demo video (2–3 min, track {Track}): {result}
> - Use case description (README + form): complete problem / user / solution
>
> {IF any Level 1 reminders — does not affect PASS: list briefly.}
>
> Next milestones: eligible list on **22/06**; voting **22/06–03/07**; award ceremony **03/07**. Any commit/deploy after 12:00 on 17/06 will not be assessed for a passed project (sec. 5.2).
>
> Good luck in the voting round!
> — Claw-a-thon 2026 Organizing Committee

---

## 4. FAIL — reasons + appeal (EN)

> **Subject:** [Claw-a-thon 2026] Assessment result — Team {Team name}: NOT PASSED (action needed)
>
> Hi team **{Team name}**,
>
> Thank you for joining Claw-a-thon 2026. After the internal assessment (Round 1), your submission **did NOT pass** for the following reason(s):
>
> {List each hard-fail reason with a rulebook citation, e.g.:
> - **A1 (sec. 6):** The AgentBase link {link} is not reachable (HTTP 404) — the agent is not running.
> - **A2 (sec. 6):** The demo video {link} cannot be opened with a VNG account / demonstrates a different track than registered ({Track}).
> - **A3 (sec. 6):** README is still the unedited template; problem/user/solution are not stated.
> - **Security (sec. 4):** A real token was found in {file} — please rotate it immediately and replace with a placeholder.}
>
> **Right to supplement:** Per section 6, your team may **appeal or supplement ONE (01) time only** during **18/06–19/06**. Please update and respond via the official BTC channel by end of 19/06. Final results will be announced on **22/06**.
>
> For technical support (account, AgentBase, deploy), contact the competition Teams channel (KimNH/VuND3).
>
> — Claw-a-thon 2026 Organizing Committee
