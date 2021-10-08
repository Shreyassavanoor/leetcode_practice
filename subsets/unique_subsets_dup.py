'''
    Given a set of numbers that might contain duplicates, find all of its distinct subsets.
    
    Example 1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]
    
    Example 2:
    Input: [1, 5, 3, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

def find_subsets_dup(nums):
    result = [[]]
    nums.sort()
    start_index, end_index = 0, 0 
    for i in range(0, len(nums)):
        start_index = 0
        if i > 0 and nums[i-1] == nums[i]:
            start_index = end_index
        end_index = len(result)
        for j in range(start_index, end_index):
            dup = list(result[j])
            dup.append(nums[i])
            result.append(dup)
    print(result)
    
if __name__ == '__main__':
    find_subsets_dup([1,3,3])
    find_subsets_dup([1,5,3,3])