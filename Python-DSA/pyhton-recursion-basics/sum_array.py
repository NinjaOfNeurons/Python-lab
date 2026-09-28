def rec_total_aray(i, nums, total):
    if(i >= len(nums)):
        # print(total)
        return

    total = total + nums[i]
    print(total, i)

    rec_total_aray(i+1, nums, total)

rec_total_aray(0,[1,2,3],0)
