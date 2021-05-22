'''
    Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

    Example 1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]
    
    Example 2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0 1 1 4 9]
'''
def square_array(arr):
    left_pointer = 0
    right_pointer = len(arr) - 1
    result = [0] * len(arr)
    index = len(arr) - 1
    
    while(left_pointer <= right_pointer):
        left_square = arr[left_pointer] * arr[left_pointer]
        right_square = arr[right_pointer] * arr[right_pointer]
        
        if left_square > right_square:
            result[index] = left_square
            index -= 1
            left_pointer += 1
        else:
            result[index] = right_square
            index -= 1
            right_pointer -= 1
    print(result)
            
if __name__ == '__main__':
    square_array([-2, -1, 0, 2, 3])
    square_array([-3, -1, 0, 1, 2])