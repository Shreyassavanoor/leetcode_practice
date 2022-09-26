'''
consider a function rev which reverses the digits in an integer.
Here are some examples:
rev(103) = 301
rev(2400) = 42
rev(9) = 9

Given an array of non-negative integers arr, your task is to count the number of pairs (i, j)
such that i ≤ j and arr[i] + rev(arr[j]) = arr[j] + rev(arr[i])

Sample input and output

for A=>[1,20,2,11],
output is 7
2.for A [4,8,20,3,10,18,5,0,13,13]
output is 21

Algo is rearrange the equation to arr[i] - rev(arr[i]) = arr[j] - rev[arr[j]]
create nums which stores arr[i] - rev(arr[i])
use hash_map to store the frequency
use nc2 formula to calculate the result

here since i <= j we need to include arr lenght
'''
from collections import Counter

def reverse_num(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev

def find_nice_numbers(nums):
    res = 0
    for i in range(len(nums)):
        nums[i] = nums[i] - reverse_num(nums[i])
        
    hash_map = Counter(nums)
    
    for val in hash_map.values():
        res += val * (val - 1) // 2
    
    print(res + len(nums))

if __name__ == "__main__":
    find_nice_numbers([1,20,2,11])
    find_nice_numbers([4,8,20,3,10,18,5,0,13,13])
