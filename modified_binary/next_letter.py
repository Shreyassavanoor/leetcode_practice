def find_next_letter(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            print(arr[(mid + 1) % len(arr)])
            return
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    print(arr[(mid + 1) % len(arr)])

if __name__ == '__main__':
    find_next_letter(['a', 'c', 'f', 'h'], 'f')
    find_next_letter(['a', 'c', 'f', 'h'], 'b')
    find_next_letter(['a', 'c', 'f', 'h'], 'm')
    find_next_letter(['a', 'c', 'f', 'h'], 'h')
    