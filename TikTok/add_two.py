def add_two_numbers(arr):
    res = []
    for i in range(1, len(arr) + 1, 2):
        res.append(arr[i] + arr[i-1])
    print(res)
    
if __name__ == '__main__':
    add_two_numbers([1,2])
    add_two_numbers([1,2, 3, 4])
    add_two_numbers([1,2, 3, 4, 5, 6, 7, 8])
    