def two_sum(nums, target):
    i = 0 
    j = len(nums) - 1
    nums = sorted(nums)
    print(nums)
    # print(i,j)
    while i<j:

        current_sum  = nums[i] + nums[j]

        if current_sum == target:
            return(nums[i],nums[j])
        elif current_sum < target:
            i += 1
        else:
            j -= 1
    return None

print(two_sum( nums = [1, 6, 2, 10, 3], target = 7))
