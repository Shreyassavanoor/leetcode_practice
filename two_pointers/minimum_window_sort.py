'''
    Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

    Example 1:
    Input: [1, 2, 5, 3, 7, 10, 9, 12]
    Output: 5
    Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
    
    Example 2:
    Input: [1, 3, 2, 0, -1, 7, 10]
    Output: 5
    Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
    
    Example 3:
    Input: [1, 2, 3]
    Output: 0
    Explanation: The array is already sorted
    
    Example 4:
    Input: [3, 2, 1]
    Output: 3
    Explanation: The whole array needs to be sorted.
'''
def find_minimum_window(arr):
    left = 0
    right = len(arr) - 1
    
    while(left < right):
        if arr[left] > arr[left + 1]:
            break
        left += 1
        
    if left == len(arr) - 1:
         print(0)
         return
    
    while(right > 0):
        if arr[right] < arr[right - 1]:
            break
        right -= 1
    
    subarray = arr[left: right + 1]
    min_ele = min(subarray)
    max_ele = max(subarray)
    
    while(left > 0 and arr[left - 1] > min_ele):
        left -= 1
    
    while(right < len(arr) - 1 and arr[right + 1] < max_ele):
        right += 1   
            
    print(right - left + 1)  

if __name__ == '__main__':
    find_minimum_window([1, 2, 5, 3, 7, 10, 9, 12])
    find_minimum_window([1, 3, 2, 0, -1, 7, 10])
    find_minimum_window([1, 2, 3])
    find_minimum_window([3, 2, 1])