def rec_str_rev(i, j , nums):
    if(i >= j):
        return nums
    
    nums[i],nums[j] = nums[j],nums[i]
    return rec_str_rev(i+1, j -1, nums)



nums = ["h","e","l","l","o"]
print(rec_str_rev(i=0,j=len(nums)-1, nums=nums))