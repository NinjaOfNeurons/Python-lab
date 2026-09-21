def rec_bubble_sort(i,nums):
    if i == len(nums) - 1:
        print(nums)
        return
     
    for j in range(len(nums)-i-1):


        if nums[j] > nums[j+1]:
            nums[j] , nums[j+1] = nums[j+1], nums[j]



    rec_bubble_sort(i+1, nums )


nums = [5,3,8,4,6]
rec_bubble_sort(0,nums)
