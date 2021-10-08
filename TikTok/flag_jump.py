#got this
def calculate_jumps(k, j):
    curr_height = 0
    result = 0

    while curr_height < k:
        if j <= k - curr_height:
            curr_height += j
        else:
            curr_height += 1
        result += 1
    
    print(result)

if __name__ == '__main__':
    calculate_jumps(8, 3)
    calculate_jumps(3, 1)
    calculate_jumps(10, 3)
    calculate_jumps(10, 6)