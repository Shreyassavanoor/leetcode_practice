'''
    Given a string and a pattern, find out if the string contains any permutation of the pattern.
    
    Example 1:
    Input: String="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.
    
    Example 2:  
    Input: String="odicf", Pattern="dc"
    Output: false
    Explanation: No permutation of the pattern is present in the given string as a substring.
    
    Example 3:    
    Input: String="bcdxabcdy", Pattern="bcdyabcdx"
    Output: true
    Explanation: Both the string and the pattern are a permutation of each other.
    
    Example 4:
    Input: String="aaacb", Pattern="abc"
    Output: true
    Explanation: The string contains "acb" which is a permutation of the given pattern.
'''
def is_permuatation(s, p):
    window_start = 0
    frequency_map_pattern = {}
    
    for pattern_char in p:
        if pattern_char not in frequency_map_pattern:
            frequency_map_pattern[pattern_char] = 0
        frequency_map_pattern[pattern_char] += 1
        
    for window_end in range(len(s)):
        if s[window_end] in frequency_map_pattern:
            frequency_map_pattern[s[window_end]] -= 1
        
        if window_end - window_start + 1 > len(p):
            if s[window_start] in frequency_map_pattern:
                frequency_map_pattern[s[window_start]] += 1
            window_start += 1
            
            if all(value == 0 for value in frequency_map_pattern.values()):
                print(True)
                return
     
    if all(value == 0 for value in frequency_map_pattern.values()):
        print(True)
        return
            
    print(False)

if __name__ == '__main__':
    is_permuatation('oidbcaf','abc')
    is_permuatation('odicf','dc')
    is_permuatation('bcdxabcdy','bcdyabcdx')
    is_permuatation('aaacb','abc')
    is_permuatation('abc','abc')