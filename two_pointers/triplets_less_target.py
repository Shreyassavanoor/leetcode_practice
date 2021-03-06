'''
    Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

    Example 1:
    Input: [-1, 0, 2, 3], target=3 
    Output: 2
    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

    Example 2:
    Input: [-1, 4, 2, 1, 3], target=5 
    Output: 4   
    Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
'''

def find_triplets(arr, target):
    arr.sort()
    x_pointer = 0
    count = 0
    
    while(x_pointer <= len(arr) - 3):
        y_pointer = x_pointer + 1
        z_pointer = len(arr) - 1 
        x = arr[x_pointer]
        
        while(y_pointer < z_pointer):
            xyz_sum = x + arr[y_pointer] + arr[z_pointer]
            
            if xyz_sum < target:
                count += z_pointer - y_pointer
                y_pointer += 1
            else:
                z_pointer -= 1
        
        x_pointer += 1 
    
    print(count)            

if __name__ == '__main__':
    find_triplets([-1, 0, 2, 3], 3)
    find_triplets([-1, 4, 2, 1, 3], 5)