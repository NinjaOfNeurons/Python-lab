def bubble_sort(nums):
    for i in range(len(nums)):
        # print(nums)
        for j in range(len(nums)-i-1):
            
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]  = nums[j+1],nums[j]
            # print(nums)
    return nums
            


            
print(bubble_sort([13,46,24,52,20,9]))