def isSorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1] and i+1 <= len(nums)-1:
            return False
    return True


print(isSorted([1,2,3,7]))


