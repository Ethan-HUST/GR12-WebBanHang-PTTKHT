# 🛒 Hệ thống Quản lý Bán hàng Siêu thị Mini – Phân tích & Thiết kế Hệ thống (MI3120)

## 🧾 Thông tin chung

- **Môn học**: Phân tích và Thiết kế Hệ thống (MI3120)  
- **Tên đề tài**: Quản lý bán hàng trên Website lĩnh vực siêu thị mini  
- **Mã lớp**: 155358  
- **Nhóm thực hiện**: Nhóm 12  
- **Giảng viên hướng dẫn**: TS. Lê Hải Hà  
- **Thời gian**: 01/2025

## 👥 Thành viên nhóm

| STT | Họ tên               | MSSV      | Nhiệm vụ chính                                                       |
|-----|----------------------|-----------|----------------------------------------------------------------------|
| 1   | Nguyễn Trung Kiên (Nhóm trưởng)    | 20227180  | Code, thuyết trình, soạn báo cáo Word/PDF và slide                  |
| 2   | Nguyễn Tuấn Anh      | 20206114  | Soạn nội dung, vẽ biểu đồ Use-case                                  |
| 3   | Lê Ngọc Trung Kiên   | 20227236  | Use-case, hoạt động, thiết kế CSDL, thuyết trình                    |
| 4   | Nguyễn Lương Phúc    | 20216869  | Soạn nội dung, biểu đồ tuần tự, thuyết trình                        |
| 5   | Lê Thế Quang         | 20227203  | Soạn nội dung, thiết kế CSDL                                        |

## 🎯 Mục tiêu đề tài

- Phân tích và thiết kế hệ thống quản lý bán hàng trực tuyến cho **siêu thị mini**.
- Xây dựng **kiến trúc ba lớp**: giao diện (UI), xử lý nghiệp vụ (Business Logic), và cơ sở dữ liệu (Data).
- Tối ưu hóa quy trình bán hàng, quản lý sản phẩm, đơn hàng, khách hàng, thanh toán, giỏ hàng, khuyến mãi.
- Áp dụng công nghệ web hiện đại: Django, Bootstrap, JavaScript, MySQL/PostgreSQL, REST API.

## 🔍 Nội dung chính

### Phần A: Giới thiệu chung
- Bối cảnh, lý do chọn đề tài, nhu cầu thực tiễn  
- Mục tiêu tổng quát và yêu cầu hệ thống (chức năng & phi chức năng)  
- Phạm vi và đối tượng áp dụng: Khách hàng, nhân viên, quản trị viên

### Phần B: Phân tích hệ thống
- Kiến trúc ba lớp (UI – Logic – Data)  
- Use-case tổng quan và phân rã  
- Biểu đồ hoạt động: đăng nhập, đăng ký, thêm sản phẩm, đặt hàng  
- Biểu đồ tuần tự: đăng nhập, đăng ký, quên mật khẩu, thêm vào giỏ hàng  
- Mô hình dữ liệu, ERD, ánh xạ thực thể – quan hệ

### Phần C: Thiết kế hệ thống
- Giao diện người dùng: đăng nhập, giỏ hàng, đặt hàng  
- Giao diện quản trị: quản lý sản phẩm, danh mục, giỏ hàng, người dùng  
- CSDL chuẩn hóa với các bảng: `KHACH_HANG`, `DON_HANG`, `SAN_PHAM`, `THANH_TOAN`, `KHUYEN_MAI`, `PHAN_HOI`, `GIO_HANG`, ...

## 🛠 Công nghệ sử dụng

- **Backend**: Django + Django REST Framework  
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript/jQuery  
- **Database**: MySQL hoặc PostgreSQL  
- **Thanh toán**: Tích hợp PayPal, Stripe  
- **Giao hàng**: Tích hợp API Giao Hàng Nhanh, GHTK  
- **Quản lý mã nguồn**: Git  
- **Triển khai môi trường**: Docker (tuỳ chọn)

## 📈 Tính năng hệ thống

- Quản lý khách hàng, giỏ hàng, đơn hàng, sản phẩm, khuyến mãi  
- Quản trị viên phân quyền và kiểm soát toàn hệ thống  
- Thống kê báo cáo doanh thu, tồn kho  
- Hệ thống phản hồi, đánh giá và xử lý bảo mật

## 📚 Tài liệu tham khảo

- Sommerville (2011) – *Software Engineering*  
- Pressman (2014) – *A Practitioner’s Approach*  
- Django Documentation: https://docs.djangoproject.com/  
- WordPress Support: https://wordpress.org/support/article/  
- Sharma & Choudhury – *Web App Development*  
- Graham – *Designing Web Usability*  
- Harrington – *Business Database Systems*

## 🙏 Lời cảm ơn

Nhóm xin trân trọng cảm ơn thầy **TS. Lê Hải Hà** vì sự hướng dẫn tận tình trong quá trình học tập và thực hiện đề tài. Qua đề tài này, nhóm đã học được quy trình thực tế trong phân tích và thiết kế hệ thống thông tin hiện đại.

---
