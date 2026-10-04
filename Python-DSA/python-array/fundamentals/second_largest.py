def scnd_lrgst(nums):
    max = -1
    second_largest = -1
    for i in range(len(nums)):
        if nums[i] > max:
            second_largest = max  #old max
            max = nums[i]         #new max
            
            # print(second_largest)
        elif nums[i] > second_largest and nums[i] != max:
            second_largest = nums[i]
            print("yo")

    print(second_largest)


scnd_lrgst([2,4,8,7,6])


