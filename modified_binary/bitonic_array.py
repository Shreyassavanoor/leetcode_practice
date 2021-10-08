'''
    Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
    
    Example 1:
    Input: [1, 3, 8, 12, 4, 2]
    Output: 12
    Explanation: The maximum number in the input bitonic array is '12'.
    
    Example 2:
    Input: [3, 8, 3, 1]
    Output: 8
    
    Example 3:
    Input: [1, 3, 8, 12]
    Output: 12
    
    Example 4:
    Input: [10, 9, 8]
    Output: 10
'''
def max_bitonic(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low+high) // 2
        
        if arr[mid] <= arr[mid+1]:
            low = mid + 1
        else:
            high = mid
    
    print(arr[high])

if __name__ == '__main__':
    max_bitonic([1, 3, 8, 12, 4, 2])
    max_bitonic([3, 8, 3, 1])
    max_bitonic([1, 3, 8, 12])
    max_bitonic([10, 9, 8])