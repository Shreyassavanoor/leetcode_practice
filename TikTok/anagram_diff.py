def find_anagram_diff(s1, s2):
    res = 0
    chars_count = [0] * 26
    
    for i in range(len(s1)):
        chars_count[ord(s1[i]) - ord('a')] += 1
    
    for i in range(len(s2)):
        chars_count[ord(s2[i]) - ord('a')] -= 1
        
    for i in range(len(chars_count)):
        if chars_count[i] != 0:
            res += abs(chars_count[i])
    
    print(res // 2)

if __name__ == '__main__':
    find_anagram_diff('abcd', 'abcc')
    find_anagram_diff('tea', 'ate')
    find_anagram_diff('act', 'acts')
    