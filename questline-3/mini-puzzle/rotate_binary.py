def rotate_binary_to_decimal(A, k):
    n = len(A)
    k = k % n
    rotated = A[-k:] + A[:-k]
    decimal_value = int(rotated, 2)
    return decimal_value
print(rotate_binary_to_decimal("1011", 1))  
print(rotate_binary_to_decimal("1011", 2))

