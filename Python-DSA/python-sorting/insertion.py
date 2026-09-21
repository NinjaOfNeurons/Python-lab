def insertion(nums):
    for i in range(1, len(nums)):
        
        j =  i 
        print(nums[i] , j, i )

        while(j > 0 ):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            else: 
                break

        print(nums)



nums  = [9,14,15,12,6,8]
print(insertion(nums))