def reverse_numbers(num):
    rev = 0
    count_zeros = 0
    
    while num > 0 and num % 10 == 0:
        count_zeros += 1
        num = num // 10
    
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    
    rev = rev * pow(10, count_zeros)
    
    print(rev)

if __name__ == "__main__":
    reverse_numbers(100)
    reverse_numbers(23450000)