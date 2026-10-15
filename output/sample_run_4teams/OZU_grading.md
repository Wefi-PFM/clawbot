# Bảng chấm Round 1 — Đội OZU

**Agent:** flight-finder-agent · **Track khai:** "Chat Agent" · **Email:** tantd2@vng.com.vn
**Repo:** https://github.com/ozuit/flight-finder-agent (public, clone OK)
**Kết luận sơ bộ:** ✅ **PASS** — *điều kiện: BTC xác nhận A1 + A2 bằng tay (xem dưới)*

---

## A. Điều kiện PASS bắt buộc (mục 6)

| | Tiêu chí | Kết quả |
|---|---|---|
| **A1** | Agent chạy trên AgentBase | ⚠️ **MANUAL** — link là endpoint AgentBase thật (`endpoint-…agentbase-runtime.aiplatform.vngcloud.vn/chat`), định dạng hợp lệ. Sandbox không truy cập được (HTTP 000 — domain VNG không trong allowlist mạng, **không phải link chết**). **BTC mở bằng tài khoản VNG và gọi thử 1 request.** |
| **A2** | Demo video hợp lệ | ⚠️ **MANUAL** — link SharePoint trong domain VNG (`vngms-my.sharepoint.com`), hợp lệ về domain. **BTC xem 2–3 phút đầu, xác nhận đúng track & end-to-end.** Lưu ý: link dán vào form bị cắt tham số `nav=` ở cuối — nếu không mở được, xin lại link đầy đủ. |
| **A3** | Mô tả use case đầy đủ | ✅ **ĐẠT** — mô tả form rất đầy đủ (Problem / Target users / How it works / Value, song ngữ VN+EN). README thật, chi tiết 357 dòng, không phải template. |

→ Không có tiêu chí A nào FAIL rõ ràng. A1 & A2 chỉ chờ BTC xác nhận thủ công.

## B. Deliverable

**B1 — README.md:** Nội dung thật, chi tiết (tính năng, cài đặt, cấu hình, chạy local, ví dụ request, tích hợp Zalo, deploy, cấu trúc dự án).
- ⚠️ Level 1: README **không có mục riêng Problem / Users / Solution / What to customize** (các ý này nằm trong mô tả form). Nên bổ sung vào README để người ngoài đọc hiểu ngay.
- ⚠️ Level 1 (model ngoài MaaS): README mặc định trỏ MaaS GreenNode AIP (tốt), nhưng `.env.example` nêu tuỳ chọn OpenAI và ví dụ `LLM_MODEL=gpt-4o-mini`. **Nếu agent thực tế deploy bằng model ngoài MaaS, phải khai báo rõ trong README** (rulebook FAQ). BTC xác nhận model đang chạy.

**B2 — Source code:** ✅ Repo public, clone OK, code đầy đủ (`main.py`, `tools/`, `integrations/zalo_bot.py`, `tests/`). Dùng `greennode-agentbase`, `langgraph`, `langchain-openai`.
- ⚠️ Level 1: Không thấy ghi nguồn nếu khởi tạo từ sample template (mục 11.2) — nếu có dùng, nên bổ sung attribution.

**B3 — demo/:** ❌ **Không có thư mục `demo/` và không có screenshot** → Level 1 nhắc nhở (video đã nộp ở form). Nên thêm `demo/` + 2–3 ảnh.

**B4 — .env.example:** ✅ Có đủ biến cần thiết (GREENNODE_CLIENT_ID/SECRET, LLM_API_KEY/BASE_URL/MODEL, SERPAPI_API_KEY, ZALO_BOT_TOKEN…), **tất cả để trống (placeholder)**. `.env` đã được `.gitignore`.

## 🔒 Quét secret

`scan_secrets.py`: **0 high, 0 medium, 3 low → không có secret thật bị lộ.**
- 3 mục "low" đều lành tính: `self.bot_token = bot_token`, `self.secret_token = secret_token` (gán tham số), và `secret_token="secret-token"` trong test. Không phải credential thật.
- *(Ghi chú: scanner ban đầu báo nhầm 3 "high" do tham chiếu biến môi trường `${ZALO_WEBHOOK_SECRET_TOKEN}` — đã xác minh là code, không phải secret.)*

## C. Hợp lệ & tuân thủ

- **Team name "OZU":** ≤60 ký tự ✅. Trùng tên giữa các đội: ⚠️ MANUAL (cần danh sách toàn cuộc).
- **Track "Chat Agent":** ⚠️ **Không khớp tên 3 track chính thức** (Agentic Assistant / Data Analysis / Automation & Integration). Khả năng cao đội định chọn **Agentic Assistant** (agent chat tìm vé, hiểu yêu cầu tự nhiên, tự truy vấn). Demo phù hợp track này. **BTC xác nhận lại tên track đúng** — không auto-fail, nhưng nên làm rõ trước trang voting.
- **Thành viên:** email `tantd2@vng.com.vn` đúng định dạng ✅. ⚠️ **Department** chưa thấy trong thông tin cung cấp — kiểm tra trong form. Trùng người ở nhiều đội: ⚠️ MANUAL.
- **Khai báo AI (mục 11.1):** UI ghi "Trợ lý AI tìm vé máy bay" / "Trợ lý tìm vé máy bay thông minh" — có ngụ ý AI. ⚠️ Level 1: nên khai báo rõ ràng hơn "bạn đang trò chuyện với AI".
- **PII / dữ liệu thật (mục 9.2):** Dùng SerpAPI (dữ liệu chuyến bay công khai) + Zalo lưu sở thích — không thấy PII thật/dữ liệu khách hàng confidential trong repo ✅. Đảm bảo demo dùng dữ liệu synthetic.
- **Copy / content policy:** Không thấy dấu hiệu vi phạm.

## D. Kết luận

**PASS (sơ bộ)** — A3 đạt rõ ràng, không có vi phạm phần C ở mức disqualify, không lộ secret. **PASS chính thức phụ thuộc BTC xác nhận A1 (gọi thử agent) và A2 (xem video đúng track).**

**Nhắc nhở Level 1 (không làm rớt, đội nên sửa):**
1. Làm rõ **tên track** đúng theo 3 lựa chọn chính thức.
2. Thêm mục **Problem / Users / Solution / What to customize** vào README.
3. Thêm thư mục **`demo/` + 2–3 screenshot**.
4. **Khai báo model**: nếu dùng model ngoài MaaS (OpenAI…), ghi rõ trong README.
5. Bổ sung **attribution** nếu khởi tạo từ sample template.
6. Khai báo **AI rõ hơn** trong UI chat.
