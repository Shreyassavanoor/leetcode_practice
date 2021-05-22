'''
    Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
    
    Example 1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
    
    Example 2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
'''
def remove_duplicates(arr):
    low = 0
    high = 0
    
    for high in range(len(arr)):
        if high > 0 and arr[high] == arr[high - 1]:
            low += 1
        if low > 0 and arr[high] != arr[high - 1]:
            arr[low] = arr[high]
            low += 1
    print(arr)
    print(low)

if __name__ == '__main__':
    remove_duplicates([2, 3, 3, 3, 6, 9, 9])
    remove_duplicates([2, 2, 2, 11])