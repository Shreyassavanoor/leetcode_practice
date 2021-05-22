'''
    Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

    Example 1:
    Input: str1="xy#z", str2="xzz#"
    Output: true
    Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
    
    Example 2:
    Input: str1="xy#z", str2="xyz#"
    Output: false
    Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
    
    Example 3:
    Input: str1="xp#", str2="xyz##"
    Output: true
    Explanation: After applying backspaces the strings become "x" and "x" respectively.
    In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
    
    Example 4:
    Input: str1="xywrrmp", str2="xywrrmu#p"
    Output: true
    Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
'''
def delete_backspace(s1):
    right = len(s1) - 1
    res = [''] * len(s1)
    count = 0
    res_index = len(s1) - 1
    
    while(right >= 0):
        if s1[right] == '#':
            count += 1
        elif count > 0:
            count -= 1
        else:
            res[res_index] = s1[right]
            res_index -= 1
        right -= 1
    
    return ''.join(res)
    
def compare_strings(s1, s2):
    result_s1 = delete_backspace(s1)
    result_s2 = delete_backspace(s2)
    
    if result_s1 == result_s2:
        print(True)
        return

    print(False)    
    
if __name__ == '__main__':
    compare_strings('xy#z', 'xzz#')
    compare_strings('xy#z', 'xyz#')
    compare_strings('xp#', 'xyz##')
    compare_strings('xywrrmp', 'xywrrmu#p')