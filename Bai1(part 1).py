import hashlib
import time

def calculate_hash(data, algorithm):
    """Tính toán hash của dữ liệu sử dụng thuật toán được chỉ định"""
    if algorithm == 'sha256':
        hash_obj = hashlib.sha256()
    elif algorithm == 'sha512':
        hash_obj = hashlib.sha512()
    else:
        raise ValueError("Thuật toán không được hỗ trợ")
    
    hash_obj.update(data.encode('utf-8'))
    return hash_obj.hexdigest()

def demonstrate_hashing():
    # Dữ liệu gốc
    original_data = "Hello, this is a test message for hashing demonstration!"
    
    # Dữ liệu đã sửa đổi (thay đổi một ký tự)
    modified_data = "Hello, this is a test message for hashing demonstration!!"
    
    print("=== DEMONSTRATION OF SHA-256 AND SHA-512 HASHING ===")
    print("\nOriginal Data:", original_data)
    print("Modified Data:", modified_data)
    
    # Tính toán và hiển thị hash SHA-256
    print("\n=== SHA-256 HASHES ===")
    original_sha256 = calculate_hash(original_data, 'sha256')
    modified_sha256 = calculate_hash(modified_data, 'sha256')
    
    print("Original Data SHA-256:", original_sha256)
    print("Modified Data SHA-256:", modified_sha256)
    print("Hash Length:", len(original_sha256) * 4, "bits")
    
    # Tính toán và hiển thị hash SHA-512
    print("\n=== SHA-512 HASHES ===")
    original_sha512 = calculate_hash(original_data, 'sha512')
    modified_sha512 = calculate_hash(modified_data, 'sha512')
    
    print("Original Data SHA-512:", original_sha512)
    print("Modified Data SHA-512:", modified_sha512)
    print("Hash Length:", len(original_sha512) * 4, "bits")
    
    # So sánh sự khác biệt
    print("\n=== COMPARISON ===")
    print("Number of different characters in SHA-256:", sum(1 for a, b in zip(original_sha256, modified_sha256) if a != b))
    print("Number of different characters in SHA-512:", sum(1 for a, b in zip(original_sha512, modified_sha512) if a != b))

def demonstrate_avalanche_effect():
    """Minh họa hiệu ứng avalanche (thay đổi nhỏ gây ra thay đổi lớn trong hash)"""
    print("\n=== AVALANCHE EFFECT DEMONSTRATION ===")
    
    # Tạo một chuỗi dài
    base_data = "A" * 1000
    
    # Thay đổi một bit ở giữa chuỗi
    modified_data = base_data[:500] + "B" + base_data[501:]
    
    # Tính hash SHA-256
    base_hash = calculate_hash(base_data, 'sha256')
    modified_hash = calculate_hash(modified_data, 'sha256')
    
    print("Original Data (first 50 chars):", base_data[:50] + "...")
    print("Modified Data (first 50 chars):", modified_data[:50] + "...")
    print("\nSHA-256 Hash of Original:", base_hash)
    print("SHA-256 Hash of Modified:", modified_hash)
    
    # Tính phần trăm thay đổi
    diff_count = sum(1 for a, b in zip(base_hash, modified_hash) if a != b)
    total_bits = len(base_hash) * 4
    change_percentage = (diff_count / total_bits) * 100
    
    print(f"\nPercentage of bits changed: {change_percentage:.2f}%")

def demonstrate_performance():
    """Minh họa hiệu suất của các thuật toán hash"""
    print("\n=== PERFORMANCE COMPARISON ===")
    
    # Tạo dữ liệu lớn
    data = "A" * 1000000  # 1MB of data
    
    # Đo thời gian SHA-256
    start_time = time.time()
    calculate_hash(data, 'sha256')
    sha256_time = time.time() - start_time
    
    # Đo thời gian SHA-512
    start_time = time.time()
    calculate_hash(data, 'sha512')
    sha512_time = time.time() - start_time
    
    print(f"SHA-256 Time: {sha256_time:.4f} seconds")
    print(f"SHA-512 Time: {sha512_time:.4f} seconds")

if __name__ == "__main__":
    demonstrate_hashing()
    demonstrate_avalanche_effect()
    demonstrate_performance() 