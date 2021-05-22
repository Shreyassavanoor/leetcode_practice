'''
    Given a string and a pattern, find all anagrams of the pattern in the given string.
    Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

    Example 1:
    Input: String="ppqp", Pattern="pq"
    Output: [1, 2]
    Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
    
    Example 2:
    Input: String="abbcabc", Pattern="abc"
    Output: [2, 3, 4]
    Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''
def find_anagrams(s, p):
    window_start = 0
    result = []
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
                result.append(window_start)
     
    # if all(value == 0 for value in frequency_map_pattern.values()):
    #     result.append(window_start)
    if len(result) == 0 and all(value == 0 for value in frequency_map_pattern.values()):
        result.append(window_start)
        
    print(result)

if __name__ == '__main__':
    find_anagrams('ppqp', 'pq')
    find_anagrams('abbcabc', 'abc')
    find_anagrams('bcdxabcdy','bcdyabcdx')