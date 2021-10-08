#cyclic sort
def cyclic_sor(nums):
    res = 0
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            res += 1
        else:
            i += 1
    print(res)
    
if __name__ == '__main__':
    cyclic_sor([7,1,3,2,4,5,6])
    cyclic_sor([4,3,1,2])