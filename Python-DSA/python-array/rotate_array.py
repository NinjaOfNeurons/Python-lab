def left_rotate(nums):
    for i in range(len(nums)):
        if i == 0:
            temp  =  nums[i]
        else:
            nums[i-1] = nums[i]

        if i == len(nums)-1:
            nums[i] = temp
    print(nums)

print(left_rotate([1,2,3,4,5,6]))

