'''
    Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

    The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

    Example 1:
    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]
    
    Example 2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0 0 1 2 2 2 ]
'''
def dutch_flag(arr):
    left, right = 0, len(arr) - 1
    i = 0
    
    while(i <= right):
        if arr[i] == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    
    print(arr) 

if __name__ == '__main__':
    dutch_flag([1, 0, 2, 1, 0])
    dutch_flag([2, 2, 0, 1, 2, 0])