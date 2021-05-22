'''
    Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
    
    Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3 
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
    
    Example 2:
    Input: [2, 3, 4, 1, 5], k=2 
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
    
    My improvement: printing array elemets 
'''
def find_max_subarray(arr, k):
    window_start, window_sum, max_sum = 0, 0, 0
    index_map = {
        'start_index': 0,
        'end_index': 0
    }
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k - 1:
            if window_sum > max_sum:
                max_sum = window_sum
                index_map['start_index'] = window_start
                index_map['end_index'] = window_end
                
            # max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    s_i = index_map['start_index']
    e_i = index_map['end_index']
    
    print(f'Max sub array sum is {max_sum} and array is {arr[s_i : e_i + 1]}')
    
    
if __name__ == '__main__':
    find_max_subarray([2, 1, 5, 1, 3, 2], 3)
    find_max_subarray([2, 3, 4, 1, 5], 2)
    