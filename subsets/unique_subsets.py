'''
    Given a set with distinct elements, find all of its distinct subsets.
    
    Example 1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]
    
    Example 2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''
def find_subsets(arr):
    result = [[]]
    for num in arr:
        res_len = len(result)
        for r in range(res_len):
            dup = list(result[r])
            dup.append(num)
            result.append(dup)
    print(result)

if __name__ == '__main__':
    find_subsets([1,3])
    find_subsets([1,5,3])