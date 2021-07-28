def remove_target(arr, target):
    left = 0
    for i in range(len(arr)):
        if i > 0 and arr[i] != arr[i-1] and arr[left] == target:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
    print(arr)
    print(left)
    
if __name__ == '__main__':
    remove_target([3, 2, 3, 6, 3, 10, 9, 3], 3)
    remove_target([2, 11, 2, 2, 1], 2)
    remove_target([2, 2, 2, 2, 2], 2)