def find_sub_strings(n, k):
    n_str = str(n)
    prev = set()
    res = 0
    
    for i in range(0, len(n_str) - k + 1):
        div = int(n_str[i:i+k])
        if div not in prev and div > 0 and n % div == 0:
            res += 1
        prev.add(div)
    print(res)
                   
if __name__ == '__main__':
    find_sub_strings(120, 2)
    find_sub_strings(555, 1)
    find_sub_strings(2345, 2)
    find_sub_strings(5341, 2)