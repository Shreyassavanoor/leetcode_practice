'''
    Given a set of distinct numbers, find all of its permutations.
    
    Example 1:
    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''
from collections import deque
def find_permutations(nums):
    result = deque()
    result.append([])
    for n in nums:
        for _ in range(0, len(result)):
            perm = list(result.popleft())
            for j in range(0, len(perm)+1):
                dup = list(perm)
                dup.insert(j, n)
                result.append(dup)
    print(list(result))

if __name__ == '__main__':
    find_permutations([1,3,5])