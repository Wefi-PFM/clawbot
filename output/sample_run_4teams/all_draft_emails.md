# Draft email kết quả Round 1 — 4 đội

> Mỗi đội một section. ⚠️ Với email PASS: chỉ gửi **sau khi BTC đã mở link xác nhận A1 (gọi thử agent) + A2 (xem video đúng track)**. Không in token/secret thật vào email.

---

## OZU — PASS ✅ (chờ xác nhận A1/A2)

**Người nhận:** tantd2@vng.com.vn
**Tiêu đề:** [Claw-a-thon 2026] Kết quả vòng đánh giá — Đội OZU: PASS ✅

Chào team **OZU**,

Cảm ơn các bạn đã hoàn thành Claw-a-thon 2026 với agent **flight-finder-agent**. Sau vòng đánh giá nội bộ (Round 1), bài nộp của đội **ĐẠT (PASS)** và đủ điều kiện vào **vòng bình chọn cộng đồng VNG Group**.

Tóm tắt kiểm tra: agent chạy trên AgentBase (đã gọi thử), demo video (SharePoint VNG) xem được đúng track, mô tả use case đầy đủ (README + form), repo public và `.env.example` chỉ chứa placeholder (không lộ token).

Lưu ý nhỏ (Level 1 — không ảnh hưởng PASS): (1) chọn đúng tên track trong 3 track chính thức — theo mô tả là *Agentic Assistant*; (2) bổ sung thư mục `demo/` + 2–3 screenshot; (3) thêm mục Problem/Users/Solution vào README; (4) nếu dùng model ngoài MaaS (OpenAI…) khai báo rõ trong README.

Mốc tiếp theo: danh sách hợp lệ **22/06**, bình chọn **22/06–03/07**, trao giải **03/07**. Mọi commit/deploy sau 12:00 ngày 17/06 không được tính cho bài đã PASS (mục 5.2).

— BTC Claw-a-thon 2026

---

## BaoBay — PASS sơ bộ ⏳ (cần xác nhận quyền truy cập repo + A1/A2)

**Người nhận:** baont9@vng.com.vn
**Tiêu đề:** [Claw-a-thon 2026] Kết quả vòng đánh giá — Đội BaoBay

Chào team **BaoBay**,

Cảm ơn bạn đã hoàn thành Claw-a-thon 2026 với agent **baobay-reply-assistant**. Mô tả use case và link agent của bạn đều ổn. Tuy nhiên BTC **chưa truy cập được link GitHub** trong form (`https://github.com/BaoNT9/baobay-reply-assistant` trả về 404 với người ngoài) — có thể repo đang ở chế độ private.

Vui lòng kiểm tra và xử lý một trong hai cách trước **12:00 ngày 17/06** (hoặc trong thời gian bổ sung 18–19/06 nếu cần): chuyển repo sang **public**, hoặc cấp quyền truy cập cho tài khoản chấm của BTC. Nếu repo mở được và có README đầy đủ, bài của bạn đạt điều kiện vào vòng bình chọn.

(Ghi nhận: agent trên AgentBase và video SharePoint của bạn ở định dạng hợp lệ — BTC sẽ xác nhận lần cuối khi mở được toàn bộ.) Lưu ý nhỏ: chọn đúng tên track trong 3 track chính thức (gần nhất: *Agentic Assistant*).

— BTC Claw-a-thon 2026

---

## Trio-CDK — PASS sơ bộ ⏳ (2 cờ cần xử lý: video & repo)

**Người nhận:** khoapnt@vng.com.vn
**Tiêu đề:** [Claw-a-thon 2026] Kết quả vòng đánh giá — Đội Trio-CDK

Chào team **Trio-CDK**,

Cảm ơn các bạn đã hoàn thành Claw-a-thon 2026 với agent **AI-Assisted Interviewer**. Mô tả use case rõ ràng và link agent AgentBase ở định dạng hợp lệ. Có **2 điểm cần xử lý** để hoàn tất đánh giá:

1. **Link GitHub** (`https://github.com/khoapnt-vng/ai-interviewer`) hiện trả về 404 với người ngoài — vui lòng chuyển repo sang public hoặc cấp quyền cho BTC.
2. **Demo video** đang để trên **Google Drive (folder)**. Theo mục 5.1, video cần đặt trên **YouTube hoặc OneDrive/SharePoint chia sẻ trong domain VNG**, và phải là **video demo 2–3 phút** (không phải folder). Vui lòng nộp lại link video đúng kênh.

Vui lòng cập nhật trước **12:00 ngày 17/06**, hoặc dùng quyền bổ sung 1 lần trong **18–19/06**. Lưu ý: chọn đúng tên track trong 3 track chính thức (gần nhất: *Agentic Assistant*).

— BTC Claw-a-thon 2026

---

## TaskForce AI — CHƯA ĐỦ CƠ SỞ ĐÁNH GIÁ ⏳ (cần bổ sung)

**Người nhận:** thuypt@vng.com.vn (CC: phuongnt3@vng.com.vn)
**Tiêu đề:** [Claw-a-thon 2026] Kết quả vòng đánh giá — Đội TaskForce AI: cần bổ sung

Chào team **TaskForce AI**,

Cảm ơn các bạn đã tham gia Claw-a-thon 2026 với agent **BOT bank RE**. Mô tả use case của đội đã rõ, nhưng BTC **chưa có cơ sở để dùng thử và xác minh agent**, nên cần các bạn bổ sung:

- **Cách dùng thử agent (A1):** trường "Link dùng thử Agent" đang trống. Nếu agent của đội chạy trên AgentBase, vui lòng gửi **link AgentBase**. Nếu đội dùng **OpenClaw chạy qua chat tool** (Zalo/Telegram/Messenger), điều này hoàn toàn hợp lệ — chỉ cần gửi **link/handle bot** để BTC nhắn thử.
- **Source code (mục 5.1):** link ở mục repo hiện là một **folder Google Drive**, không phải repository (GitHub/internal git). Vui lòng gửi link repo chứa source code.
- **Demo video (mục 5.1):** video cũng trỏ vào **cùng folder Google Drive** — cần là video 2–3 phút trên YouTube hoặc OneDrive/SharePoint trong domain VNG.

**Quyền bổ sung:** Theo mục 6, đội được **appeal hoặc bổ sung MỘT (01) lần duy nhất** trong **18–19/06**. Vui lòng bổ sung 3 mục trên qua kênh chính thức của BTC trước hết ngày 19/06; nếu agent dùng thử được, bài sẽ được xét PASS. Kết quả cuối công bố **22/06**.

Hỗ trợ kỹ thuật (account,