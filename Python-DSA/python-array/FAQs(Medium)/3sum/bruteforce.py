def three_sum(nums, target):
    result = set()

    for i in range(len(nums)):
        j = i +1
        for j  in range(len(nums)):
            k = j+1
            for k  in range(len(nums)):
                if nums[i]+nums[j]+nums[k] == target:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return result
            






print(three_sum([2, -2, 0, 3, -3, 5], 0))