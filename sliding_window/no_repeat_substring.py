'''
    Given a string, find the length of the longest substring which has no repeating characters.

    Example 1:
    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating characters is "abc".
    
    Example 2:
    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring without any repeating characters is "ab".
    
    Example 3:    
    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''
def find_longest_substring(s):
    window_start, max_length = 0, 0
    frequency_map = {}
    
    for window_end in range(len(s)):
        if s[window_end] not in frequency_map:
            frequency_map[s[window_end]] = 0
        frequency_map[s[window_end]] += 1
        
        while frequency_map[s[window_end]] > 1:
            frequency_map[s[window_start]] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
        
    print(f'Longest substring length without any repeating characters is {max_length}')    
    
if __name__ == '__main__':
    find_longest_substring('aabccbb')
    find_longest_substring('abbbb')
    find_longest_substring('abccde')
    find_longest_substring('ehkejbfabfajmssdbhcbvsdsasas')