import hashlib
import os
import json

def tinh_hash_file(file_path, algorithm='sha256'):
    """Tính hash của file sử dụng SHA-256 hoặc SHA-512"""
    try:
        # Chuẩn hóa đường dẫn file
        file_path = os.path.normpath(file_path)
        
        # Kiểm tra file có tồn tại không
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Không tìm thấy file: {file_path}")
            
        # Tạo đối tượng hash
        if algorithm == 'sha256':
            hash_obj = hashlib.sha256()
        elif algorithm == 'sha512':
            hash_obj = hashlib.sha512()
        else:
            raise ValueError("Chỉ hỗ trợ SHA-256 và SHA-512")
        
        # Đọc và băm file theo từng block
        with open(file_path, 'rb') as f:
            # Đọc file theo block 4096 bytes
            for block in iter(lambda: f.read(4096), b''):
                hash_obj.update(block)
                
        return hash_obj.hexdigest()
        
    except Exception as e:
        print(f"Lỗi khi xử lý file: {str(e)}")
        return None

def doc_hash_file(hash_file='file_hashes.json'):
    """Đọc dữ liệu hash từ file JSON"""
    try:
        if not os.path.exists(hash_file):
            return {}
            
        with open(hash_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:  # Nếu file rỗng
                return {}
            return json.loads(content)
    except json.JSONDecodeError:
        print("File hash bị lỗi, tạo file mới")
        return {}
    except Exception as e:
        print(f"Lỗi khi đọc file hash: {str(e)}")
        return {}

def luu_hash(file_path, hash_file='file_hashes.json'):
    """Lưu hash của file vào file JSON"""
    try:
        # Chuẩn hóa đường dẫn file
        file_path = os.path.normpath(file_path)
        
        # Tính hash SHA-256 và SHA-512
        sha256_hash = tinh_hash_file(file_path, 'sha256')
        sha512_hash = tinh_hash_file(file_path, 'sha512')
        
        if not sha256_hash or not sha512_hash:
            return False
            
        # Đọc dữ liệu hash hiện có
        hash_data = doc_hash_file(hash_file)
        
        # Cập nhật hash mới
        hash_data[file_path] = {
            'sha256': sha256_hash,
            'sha512': sha512_hash
        }
        
        # Lưu vào file
        with open(hash_file, 'w', encoding='utf-8') as f:
            json.dump(hash_data, f, indent=4, ensure_ascii=False)
            
        print(f"Đã lưu hash cho file: {file_path}")
        print(f"SHA-256: {sha256_hash}")
        print(f"SHA-512: {sha512_hash}")
        return True
        
    except Exception as e:
        print(f"Lỗi khi lưu hash: {str(e)}")
        return False

def kiem_tra_toan_ven(file_path, hash_file='file_hashes.json'):
    """Kiểm tra tính toàn vẹn của file bằng cách so sánh hash"""
    try:
        # Chuẩn hóa đường dẫn file
        file_path = os.path.normpath(file_path)
        print(f"\nĐường dẫn file đã chuẩn hóa: {file_path}")
        
        # Đọc dữ liệu hash
        hash_data = doc_hash_file(hash_file)
        
        # In ra danh sách các file đã lưu hash
        if hash_data:
            print("\nCác file đã lưu hash:")
            for saved_path in hash_data.keys():
                print(f"- {saved_path}")
        else:
            print("\nChưa có file nào được lưu hash!")
            return False
            
        # Kiểm tra file có trong dữ liệu hash không
        if file_path not in hash_data:
            print(f"\nKhông tìm thấy hash của file: {file_path}")
            print("Hãy chọn chức năng 2 để lưu hash của file trước khi kiểm tra!")
            return False
            
        # Tính hash hiện tại
        print("\nĐang tính hash hiện tại của file...")
        current_sha256 = tinh_hash_file(file_path, 'sha256')
        current_sha512 = tinh_hash_file(file_path, 'sha512')
        
        if not current_sha256 or not current_sha512:
            return False
            
        # So sánh hash
        original_hashes = hash_data[file_path]
        sha256_match = current_sha256 == original_hashes['sha256']
        sha512_match = current_sha512 == original_hashes['sha512']
        
        print("\n=== KẾT QUẢ KIỂM TRA TOÀN VẸN ===")
        print(f"File: {file_path}")
        print(f"SHA-256: {'✓ Khớp' if sha256_match else '✗ Không khớp'}")
        print(f"SHA-512: {'✓ Khớp' if sha512_match else '✗ Không khớp'}")
        
        if sha256_match and sha512_match:
            print("\n✓ File không bị thay đổi!")
        else:
            print("\n✗ File đã bị thay đổi!")
            print("\nHash gốc:")
            print(f"SHA-256: {original_hashes['sha256']}")
            print(f"SHA-512: {original_hashes['sha512']}")
            print("\nHash hiện tại:")
            print(f"SHA-256: {current_sha256}")
            print(f"SHA-512: {current_sha512}")
        
        return sha256_match and sha512_match
        
    except Exception as e:
        print(f"Lỗi khi kiểm tra toàn vẹn: {str(e)}")
        return False

def main():
    print("=== CHƯƠNG TRÌNH BĂM VÀ KIỂM TRA TOÀN VẸN FILE ẢNH ===")
    
    while True:
        print("\n1. Tính hash file")
        print("2. Lưu hash file")
        print("3. Kiểm tra toàn vẹn file")
        print("4. Thoát")
        
        choice = input("\nChọn chức năng (1-4): ").strip()
        
        if choice == '4':
            break
            
        # Nhập đường dẫn file
        file_path = input("\nNhập đường dẫn file ảnh: ").strip()
        
        # Kiểm tra file có tồn tại không
        if not os.path.exists(file_path):
            print("File không tồn tại!")
            continue
            
        if choice == '1':
            # Tính hash SHA-256
            print("\n=== KẾT QUẢ BĂM SHA-256 ===")
            sha256_hash = tinh_hash_file(file_path, 'sha256')
            if sha256_hash:
                print(f"Độ dài hash: {len(sha256_hash) * 4} bits")
                print(f"Giá trị hash: {sha256_hash}")
            
            # Tính hash SHA-512
            print("\n=== KẾT QUẢ BĂM SHA-512 ===")
            sha512_hash = tinh_hash_file(file_path, 'sha512')
            if sha512_hash:
                print(f"Độ dài hash: {len(sha512_hash) * 4} bits")
                print(f"Giá trị hash: {sha512_hash}")
                
        elif choice == '2':
            if luu_hash(file_path):
                print("Đã lưu hash thành công!")
            else:
                print("Lưu hash thất bại!")
                
        elif choice == '3':
            kiem_tra_toan_ven(file_path)
            
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main() 