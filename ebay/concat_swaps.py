def concat_swaps(s, size):
    result = ''
    swap = ''
    prev = -1
    
    for i, v in enumerate(size):
        if prev > -1:
            req_str = s[prev:prev+v]
            swap = req_str + swap
            if i % 2 == 1:
                result += swap
                swap = ''
            prev = prev + v
        else:
            req_str = s[0:v]
            swap += req_str
            prev = v
    
    result += swap
    print(result)
            

if __name__ == '__main__':
    concat_swaps('descognail', [3,2,3,1,1])
    concat_swaps('secondfirst', [6,5])
    concat_swaps('shreyas', [1,2,3,1])