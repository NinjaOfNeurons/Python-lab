def rec_insertion(nums , i):

    if(i > len(nums)-1):
        print(nums)
        return nums
  
    key =  nums[i]
    j = i - 1

    while(j>=0 and nums[j]>key):
        nums[j+1] = nums [j]

        j -= 1

    nums[j+1] = key

    rec_insertion(nums,i+1)



print(rec_insertion([4, 2, 3, 1], 0))

