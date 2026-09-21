def freq_count(nums):
    freq_dic ={}
    for num in nums:
        freq_dic[num] = freq_dic.get(num,0)+1


    mums = []
    for key,value in freq_dic.items():
        mums.append([key,value])

    # print(mums)



    return mums

print(freq_count([3,2,3,4,3,1,2,2]))

