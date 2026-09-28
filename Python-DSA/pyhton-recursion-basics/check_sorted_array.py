def is_array_sorted(i, nums):
    if(i  >= len(nums)-1):
        return True 

    if(nums[i] > nums[i+1]):
        return False

    # print(i,i+1)
    return is_array_sorted(i+1, nums)
    


print(is_array_sorted(i=0,nums=[1,2,3,4,5,4]))