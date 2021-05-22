'''
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

    Example 1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".
    
    Example 2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".
    
    Example 3:
    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
    
    Similar problem:
    1. Fruits in basket
    2. Longest Substring with at most 2 distinct characters
'''

def find_longest_substring(str, k):
    window_start, max_length = 0, 0
    frequency_map = {}
    
    for window_end in range(len(str)):
        if str[window_end] not in frequency_map:
            frequency_map[str[window_end]] = 0
        frequency_map[str[window_end]] += 1
        
        while len(frequency_map) > k:
            frequency_map[str[window_end]] -= 1
            if frequency_map[str[window_end]] == 0:
                del frequency_map[str[window_end]]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
        
    print(f'The longest substrings with no more than {k} distinct characters is {max_length}')

if __name__ == '__main__':
    find_longest_substring('araaci', 2)
    find_longest_substring('araaci', 1)
    find_longest_substring('cbbebi', 3)