import hashlib

def hash_data(data, algorithm='sha256'):
    """Hàm băm dữ liệu sử dụng SHA-256 hoặc SHA-512"""
    if algorithm == 'sha256':
        hash_obj = hashlib.sha256()
    elif algorithm == 'sha512':
        hash_obj = hashlib.sha512()
    else:
        raise ValueError("Chỉ hỗ trợ SHA-256 và SHA-512")
    
    # Cập nhật dữ liệu vào đối tượng hash
    hash_obj.update(data.encode('utf-8'))
    
    # Trả về giá trị hash dưới dạng chuỗi hex
    return hash_obj.hexdigest()

def main():
    # Nhập dữ liệu từ người dùng
    print("=== CHƯƠNG TRÌNH BĂM DỮ LIỆU SHA-256 VÀ SHA-512 ===")
    data = input("\nNhập dữ liệu cần băm: ")
    
    # Băm dữ liệu với SHA-256
    sha256_hash = hash_data(data, 'sha256')
    print("\n=== KẾT QUẢ BĂM SHA-256 ===")
    print(f"Độ dài hash: {len(sha256_hash) * 4} bits")
    print(f"Giá trị hash: {sha256_hash}")
    
    # Băm dữ liệu với SHA-512
    sha512_hash = hash_data(data, 'sha512')
    print("\n=== KẾT QUẢ BĂM SHA-512 ===")
    print(f"Độ dài hash: {len(sha512_hash) * 4} bits")
    print(f"Giá trị hash: {sha512_hash}")
    
    # Thử nghiệm với dữ liệu đã sửa đổi
    modified_data = data + "1"  # Thêm số 1 vào cuối
    print("\n=== THỬ NGHIỆM VỚI DỮ LIỆU ĐÃ SỬA ĐỔI ===")
    print(f"Dữ liệu gốc: {data}")
    print(f"Dữ liệu đã sửa: {modified_data}")
    
    # Băm dữ liệu đã sửa
    modified_sha256 = hash_data(modified_data, 'sha256')
    modified_sha512 = hash_data(modified_data, 'sha512')
    
    # So sánh kết quả
    print("\n=== SO SÁNH KẾT QUẢ ===")
    print("SHA-256:")
    print(f"Hash gốc:     {sha256_hash}")
    print(f"Hash đã sửa:  {modified_sha256}")
    print(f"Số ký tự khác nhau: {sum(1 for a, b in zip(sha256_hash, modified_sha256) if a != b)}")
    
    print("\nSHA-512:")
    print(f"Hash gốc:     {sha512_hash}")
    print(f"Hash đã sửa:  {modified_sha512}")
    print(f"Số ký tự khác nhau: {sum(1 for a, b in zip(sha512_hash, modified_sha512) if a != b)}")

if __name__ == "__main__":
    main() 