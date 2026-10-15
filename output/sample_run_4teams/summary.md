# Bảng tổng hợp chấm Round 1 — 4 đội

*Chấm theo trạng thái repo lúc form đóng. A1/A2 luôn cần BTC mở link bằng tài khoản VNG để chốt (xem `all_draft_emails.md`).*

| Đội | Kết quả | A1 — AgentBase | A2 — Video | A3 — Mô tả | Secret | Lưu ý / Level 1 |
|---|---|---|---|---|---|---|
| **OZU** | ✅ **PASS** (chờ A1/A2) | ⚠️ MANUAL — endpoint hợp lệ | ⚠️ MANUAL — SharePoint VNG | ✅ đủ | CLEAN | thiếu `demo/`; track "Chat Agent"; xác nhận model (MaaS/OpenAI) |
| **BaoBay** | ⏳ **PASS sơ bộ** (chờ A1/A2 + repo) | ⚠️ MANUAL — endpoint hợp lệ | ⚠️ MANUAL — SharePoint VNG | ✅ form (README chưa xác minh) | chưa quét được | **repo GitHub trả 404** → BTC xác nhận quyền truy cập; track |
| **Trio-CDK** | ⏳ **PASS sơ bộ** (chờ A1/A2 + 2 cờ) | ⚠️ MANUAL — endpoint hợp lệ | ⚠️ **cờ** — video trên Google Drive (không phải YouTube/OneDrive VNG) | ✅ form (README chưa xác minh) | chưa quét được | **repo GitHub trả 404**; video sai kênh; track |
| **TaskForce AI** | ⏳ **PENDING** (cần bổ sung) | ⚠️ không có URL AgentBase — kiểm xem có chạy qua chat tool (Zalo/Telegram) không | ⚠️ video Google Drive (trùng link "repo") | ✅ form | chưa quét được | thiếu cách dùng thử (URL hoặc link bot) + repo git + video đúng kênh; track |

## Diễn giải nhanh

- **OZU** là bài hoàn chỉnh nhất: chỉ chờ BTC gọi thử agent + xem video là chốt PASS.
- **BaoBay & Trio-CDK**: link agent + mô tả ổn, nhưng **link GitHub trả 404** với người ngoài → có thể là repo private/internal (rulebook cho phép internal). BTC cần mở link repo bằng quyền truy cập phù hợp; nếu vào được và có README đúng → PASS. Riêng **Trio-CDK** còn để **video trên Google Drive** — không đúng kênh quy định (YouTube hoặc OneDrive/SharePoint trong domain VNG), và là "folder" chứ không phải file video → BTC kiểm kỹ A2.
- **TaskForce AI**: **không có link dùng thử agent**. Lưu ý theo tiêu chí mới: thiếu URL AgentBase KHÔNG tự động FAIL nếu agent chạy qua chat tool (Zalo/Telegram) — nhưng đội cũng **không cung cấp link/handle bot**, và "repo" lẫn "video" đều trỏ vào **cùng một folder Google Drive** (không phải repo git, không phải video demo hợp lệ). Vì vậy hiện **chưa đủ cơ sở để dùng thử agent và xác minh** → để **PENDING**, yêu cầu bổ sung trong 18–19/06: (1) cách dùng thử (URL AgentBase HOẶC link bot chat tool), (2) repo git, (3) video đúng kênh. Nếu bổ sung đủ và agent chạy được → PASS.

## L�