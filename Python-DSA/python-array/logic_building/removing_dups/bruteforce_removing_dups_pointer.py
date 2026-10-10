def remove_dups_pointer(nums):
    i = 0  
    j = 1

    while(i < len(nums) -1 and j <= len(nums) -1):
        if nums[i] == nums[j]:
            j += 1
        else:
            i +=1
            nums[i]  =  nums[j]


    while i + 1 < len(nums):
        nums[i + 1] = 0
        i += 1

        
    return nums




nums = [0, 0, 3, 3, 5, 6]
print(remove_dups_pointer(nums))