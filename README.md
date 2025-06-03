# Chương Trình Băm và Kiểm Tra Toàn Vẹn Dữ Liệu

Bộ chương trình này bao gồm các công cụ để băm dữ liệu và kiểm tra tính toàn vẹn của file sử dụng các thuật toán SHA-256 và SHA-512.

## Các Chương Trình

### 1. Bai1(part 1).py - Minh Họa Hàm Băm
Chương trình này minh họa các tính chất của hàm băm SHA-256 và SHA-512:

- Tính toán hash cho dữ liệu gốc và dữ liệu đã sửa đổi
- Minh họa hiệu ứng avalanche (thay đổi nhỏ gây ra thay đổi lớn trong hash)
- So sánh hiệu suất giữa SHA-256 và SHA-512

#### Tính năng:
- Tính toán và hiển thị hash SHA-256 và SHA-512
- So sánh số lượng ký tự khác nhau giữa các hash
- Minh họa hiệu ứng avalanche với dữ liệu lớn
- Đo thời gian xử lý của mỗi thuật toán

### 2. Bai1(part 2).py - Chương Trình Băm Dữ Liệu Đơn Giản
Chương trình tương tác cho phép người dùng nhập dữ liệu và xem kết quả băm:

- Hỗ trợ cả SHA-256 và SHA-512
- Hiển thị độ dài và giá trị hash
- So sánh kết quả băm giữa dữ liệu gốc và dữ liệu đã sửa đổi

### 3. Bai 2.py - Chương Trình Kiểm Tra Toàn Vẹn File
Chương trình nâng cao để quản lý và kiểm tra tính toàn vẹn của file:

#### Tính năng chính:
1. **Tính hash file**
   - Tính toán hash SHA-256 và SHA-512 cho file
   - Hiển thị độ dài và giá trị hash

2. **Lưu hash file**
   - Lưu hash của file vào file JSON
   - Hỗ trợ nhiều file cùng lúc
   - Lưu cả hash SHA-256 và SHA-512

3. **Kiểm tra toàn vẹn file**
   - So sánh hash hiện tại với hash đã lưu
   - Hiển thị kết quả chi tiết về tính toàn vẹn
   - Cảnh báo khi file bị thay đổi

## Cách Sử Dụng

### Cài đặt
Chương trình sử dụng thư viện chuẩn của Python, không cần cài đặt thêm thư viện.

### Chạy chương trình
1. **Bai1(part 1).py**:
   ```bash
   python "Bai1(part 1).py"
   ```

2. **Bai1(part 2).py**:
   ```bash
   python "Bai1(part 2).py"
   ```

3. **Bai 2.py**:
   ```bash
   python "Bai 2.py"
   ```

### Hướng dẫn sử dụng Bai 2.py
1. Chọn chức năng từ menu:
   - 1: Tính hash file
   - 2: Lưu hash file
   - 3: Kiểm tra toàn vẹn file
   - 4: Thoát

2. Nhập đường dẫn file cần xử lý
3. Xem kết quả và thực hiện các bước tiếp theo

## Lưu ý
- File hash được lưu trong `file_hashes.json`
- Đảm bảo có quyền đọc/ghi file trong thư mục làm việc
- Nên lưu hash của file trước khi kiểm tra toàn vẹn

## Yêu cầu hệ thống
- Python 3.x
- Hệ điều hành: Windows/Linux/MacOS

## Giải thích Thuật Ngữ

### Hash (Hàm Băm)
- Là một chuỗi ký tự có độ dài cố định được tạo ra từ dữ liệu đầu vào
- Có tính chất một chiều: không thể suy ngược lại dữ liệu gốc từ hash
- Có tính chất avalanche: thay đổi nhỏ trong dữ liệu gốc sẽ tạo ra hash hoàn toàn khác

### SHA-256 và SHA-512
- SHA-256: tạo ra hash 256 bit (64 ký tự hex)
- SHA-512: tạo ra hash 512 bit (128 ký tự hex)
- Cả hai đều là các thuật toán băm an toàn, được sử dụng rộng rãi trong bảo mật

### Tính Toàn Vẹn File
- Đảm bảo file không bị thay đổi trái phép
- Được kiểm tra bằng cách so sánh hash hiện tại với hash gốc
- Nếu hash khác nhau, file đã bị thay đổi

## Xử Lý Lỗi
- Nếu file không tồn tại: chương trình sẽ thông báo lỗi
- Nếu không có quyền truy cập: kiểm tra quyền đọc/ghi file
- Nếu file hash bị hỏng: chương trình sẽ tạo file hash mới

## Bảo Mật
- Hash được lưu trong file JSON có thể bị chỉnh sửa
- Nên bảo vệ file `file_hashes.json` để tránh bị giả mạo
- Có thể mã hóa file hash để tăng tính bảo mật
