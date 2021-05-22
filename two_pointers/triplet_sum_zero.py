'''
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
    
    Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    Explanation: There are four unique triplets whose sum is equal to zero.
    
    Example 2:
    Input: [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.
'''
def find_triplets_zero_sum(arr):
    arr.sort()
    x_pointer = 0
    
    while(x_pointer <= len(arr) - 3):
        y_pointer = x_pointer + 1
        z_pointer = len(arr) - 1 
        
        #skip same element to avoid duplicates
        if x_pointer > 0 and arr[x_pointer] == arr[x_pointer - 1]:
            x_pointer += 1 
            continue
        
        x = arr[x_pointer]
        target = 0 - x
        
        while(y_pointer < z_pointer):
            yz_sum = arr[y_pointer] + arr[z_pointer]
            
            if yz_sum == target:
                print([arr[x_pointer], arr[y_pointer], arr[z_pointer]])
                y_pointer += 1
                z_pointer -= 1
                
                #skip same element to avoid duplicates
                while y_pointer < z_pointer and arr[y_pointer] == arr[y_pointer - 1]:
                    y_pointer += 1
                
                #skip same element to avoid duplicates    
                while y_pointer < z_pointer and arr[z_pointer] == arr[z_pointer + 1]:
                    z_pointer -= 1
                continue
            
            if yz_sum > target:
                z_pointer -= 1
            else:
                y_pointer += 1
        
        x_pointer += 1             

if __name__ == '__main__':
    find_triplets_zero_sum([-3, 0, 1, 2, -1, 1, -2])
    find_triplets_zero_sum([-5, 2, -1, -2, 3])
    find_triplets_zero_sum([1,1,1,-1,0, 0, 0, 0])