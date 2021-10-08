def find_goodtuples(arr):
    hash_map = {}
    w_s = 0
    res = 0
    for w_e in range(len(arr)):
        if arr[w_e] not in hash_map:
            hash_map[arr[w_e]] = 0
        hash_map[arr[w_e]] += 1
        
        if (w_e - w_s + 1) == 3:
            if len(hash_map) == 2:
                res += 1
            hash_map[arr[w_s]] -= 1
            if hash_map[arr[w_s]] == 0:
                del hash_map[arr[w_s]]
            w_s += 1
    
    print(res)

if __name__ == '__main__':
    find_goodtuples([1, 1, 2, 1, 5, 3, 2, 3])
    find_goodtuples([2,2,3,2,2,3,4,3,4])