'''
    Given a string, find all of its permutations preserving the character sequence but changing case.
    Example 1:
    Input: "ad52"
    Output: "ad52", "Ad52", "aD52", "AD52" 
    
    Example 2:
    Input: "ab7c"
    Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''
from collections import deque
def perm_case(word):
    result = []
    queue = deque([[]])
    for w in word:
        for q in range(0, len(queue)):
            dup = list(queue.popleft())
            for i in range(0,2):
                dup1 = list(dup)
                if i == 0:
                    dup1.append(w)
                else:
                    dup1.append(w.swapcase())
                queue.append(dup1)
    perm_set = set()
    for w in queue:
        w_c = ''.join(w)
        if w_c not in perm_set:
            print(w_c)
            perm_set.add(w_c) 

if __name__ == '__main__':
    # perm_case('ad52')
    perm_case('ab7c')