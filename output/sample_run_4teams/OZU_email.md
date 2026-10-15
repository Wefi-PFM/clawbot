# Draft email — Đội OZU

> ⚠️ **BTC lưu ý trước khi gửi:** Đây là email PASS. Chỉ gửi **sau khi đã xác nhận thủ công**:
> (1) mở link AgentBase bằng tài khoản VNG và gọi thử 1 request thành công (A1);
> (2) xem được video demo, đúng track (A2).
> Nếu A1 hoặc A2 không đạt → chuyển sang dùng template FAIL và nêu rõ mục chưa đạt.

---

**Tiêu đề:** [Claw-a-thon 2026] Kết quả vòng đánh giá — Đội OZU: PASS ✅

Chào team **OZU**,

Cảm ơn các bạn đã hoàn thành Claw-a-thon 2026 với agent **flight-finder-agent**. Sau vòng đánh giá nội bộ (Round 1), bài nộp của đội **ĐẠT (PASS)** và đủ điều kiện vào **vòng bình chọn cộng đồng VNG Group**.

Tóm tắt kiểm tra:
- Agent chạy trên AgentBase: đã truy cập và gọi thử thành công.
- Demo video (SharePoint VNG): xem được, đúng track đã đăng ký.
- Mô tả use case (README + form): đầy đủ problem / user / solution / value.
- Source & cấu hình: repo public, `.env.example` chỉ chứa placeholder, không lộ token thật.

Một vài lưu ý nhỏ (Level 1 — **không ảnh hưởng kết quả PASS**, đội nên hoàn thiện trước khi trang voting public):
1. **Tên track:** vui lòng chọn đúng 1 trong 3 track chính thức — *Agentic Assistant / Data Analysis / Automation & Integration*. "Chat Agent" không nằm trong danh sách; theo mô tả, agent của đội phù hợp **Agentic Assistant** — đội xác nhận lại giúp BTC.
2. **README:** nên bổ sung mục Problem / Users / Solution / What to customize để người ngoài đọc README hiểu ngay.
3. **demo/**: thêm thư mục `demo/` kèm 2–3 screenshot của agent.
4. **Khai báo model:** nếu agent dùng model ngoài MaaS (OpenAI…), khai báo rõ trong README (theo FAQ rulebook).
5. **Khai báo AI:** nên hiển thị rõ với người dùng cuối rằng họ đang trò chuyện với AI (mục 11.1).

Các mốc tiếp theo: danh sách bài hợp lệ công bố **22/06**; bình chọn **22/06–03/07**; trao giải **03/07**. Lưu ý mọi commit/deploy sau 12:00 ngày 17/06 sẽ không được tính cho bài đã PASS (mục 5.2).

Chúc đội may mắn ở vòng bình chọn!
— BTC Claw-a-thon 2026
