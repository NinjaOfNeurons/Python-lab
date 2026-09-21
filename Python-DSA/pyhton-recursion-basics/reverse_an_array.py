def reverse_arry(nums, i, nums2):
    if(i < 0):
        print(nums2)
        return

    nums2.append(nums[i])

    reverse_arry(nums,i-1,nums2)








nums = [3,4,5,9]
reverse_arry(nums, i=len(nums)-1,nums2=[])


