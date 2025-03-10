def palindrome(n):
    original_num = n
    revese_num = 0
    while (n > 0):
        part_num = n % 10
        revese_num = revese_num * 10 + part_num
        n = n // 10
    return revese_num == original_num
    
def large_palindrom():
    large_num = 0
    for i in range(999 , 99 , -1):
        for j in range(i, 99, -1):
            new_num = i * j
            if new_num <= large_num:
                break
            if palindrome(new_num):
                large_num = new_num
    return large_num

print(large_palindrom())
