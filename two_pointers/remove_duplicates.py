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

#version 1
def remove_duplicates(arr):
    index = 1
    left = 1
    
    while(index < len(arr)):
        if arr[left - 1] != arr[index]:
            arr[left] = arr[index]
            left += 1
        index += 1
    print(arr)

#version 2 my version
def remove_duplicates_v2(arr):
    left = 0
    index = 0
    
    while(index < len(arr)):
        if index > 0:
            if arr[index] != arr[left]:
                left += 1
                if left > 0:
                    arr[left] = arr[index]
        index += 1

    print(left + 1)
    
#version 3 my version
def remove_duplicates_v3(arr):
    left = 0
    for i in range(len(arr)):
        if i > 0 and arr[i] != arr[left]:
            left += 1
            arr[left], arr[i] = arr[i], arr[left]
    print(arr)
    print(left + 1)
        
if __name__ == '__main__':
    # remove_duplicates([2, 3, 3, 3, 6, 9, 9])
    # remove_duplicates([2, 2, 2, 11])
    # remove_duplicates_v2([2, 3, 3, 3, 6, 9, 9])
    # remove_duplicates_v2([2, 2, 2, 11])
    # remove_duplicates_v2([1, 1, 1, 2, 3, 4, 4, 4, 5])
    remove_duplicates_v3([2, 3, 3, 3, 6, 9, 9])
    remove_duplicates_v3([2, 2, 2, 11])
    remove_duplicates_v3([1, 1, 1, 2, 3, 4, 4, 4, 5])
    remove_duplicates_v3([0,0,0,0,0])