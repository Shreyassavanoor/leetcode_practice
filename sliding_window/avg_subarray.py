''' 
    Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
'''

def find_average(arr, k):
    avg_list = []
    window_start, window_sum = 0, 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k - 1:
            avg_list.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1
            
    print(f'Average is {avg_list}')

if __name__ == '__main__':
    find_average([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)