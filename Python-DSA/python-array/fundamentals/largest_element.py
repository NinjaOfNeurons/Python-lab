def largest_element(nums):
    max = 0
    for i in range(len(nums)):
        if nums[i] >  max:
            max = nums[i]
        return max
print(largest_element([2,3,4,1,36,7]))