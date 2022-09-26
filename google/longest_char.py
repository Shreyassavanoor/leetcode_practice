def longest_str(s):
    max_len = 0
    start_index = 0
    end_index = 0
    chars_map = {}
    
    for index, c in enumerate(s):
        if c not in chars_map:
            chars_map[c] = index
        curr_len = index - chars_map[c] + 1
        if curr_len >= max_len:
            max_len = curr_len
            start_index = chars_map[c]
            end_index = index
    print(s[start_index: end_index + 1])

if __name__ == '__main__':
    longest_str([])