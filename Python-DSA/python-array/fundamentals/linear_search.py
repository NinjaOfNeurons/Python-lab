def lnr_src(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i + 1
    return None

print(lnr_src([2,2,4,3,6], 3))