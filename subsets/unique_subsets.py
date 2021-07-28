'''
    Given a set with distinct elements, find all of its distinct subsets.
    
    Example 1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]
    
    Example 2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''
def find_subsets(nums):
    result = [[]]
    for num in nums:
        n = len(result)
        for i in range(n):
            sub_set = list(result[i])
            sub_set.append(num)
            result.append(sub_set)
    print(result)
        
if __name__ == '__main__':
    find_subsets([1,3])