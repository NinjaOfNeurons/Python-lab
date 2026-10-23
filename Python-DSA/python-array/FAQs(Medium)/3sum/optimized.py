def three_sum(nums, target):
    result = set()
    nums.sort()
    for k in range(len(nums)):    
        j = len(nums)-1
        i = k + 1
        while(i<j):
            sum_nums  = nums[i]  + nums[j] + nums[k]
            # print(sum_nums)
            if sum_nums == target:
                triplet = (nums[k], nums[i], nums[j])
                result.add(triplet)
                i += 1
                j -= 1
                
                # return(nums[i],nums[j],nums[k])
            elif sum_nums < target:
                i += 1
            else:
                j -= 1
    return result 








print(three_sum(nums = [2, -2, 0, 3, -3, 5], target = 0))