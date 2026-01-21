# W5A8
def hamming_distance(str1, str2):
    # Đảm bảo cả hai chuỗi có độ dài bằng nhau
    if len(str1) != len(str2):
        raise ValueError("Hai chuỗi phải có độ dài bằng nhau")
    
    # Tính số lượng ký tự khác nhau tại mỗi vị trí
    distance = sum(1 for a, b in zip(str1, str2) if a != b)
    return distance
print(hamming_distance("abc", "abd"))


print()
# W5AA7
def hamming_distance(x, y):
    return bin(x ^ y).count('1')
print(hamming_distance(10, 15))



print()
# W5A5
def find_greater_than_k(lst, k):
    for i, num in enumerate(lst):
        if num > k:
            return i
    return -1
print(find_greater_than_k([1, 3, 5, 7], 4))