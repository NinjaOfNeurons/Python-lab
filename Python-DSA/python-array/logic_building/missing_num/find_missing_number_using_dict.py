def missingNumber(nums):
    num_dic = {}
    for num in nums:
        num_dic[num] = 1
    print(num_dic)
    for i in range(len(nums)+1):
        if i not in num_dic:
            return(i)
      
print(missingNumber( [0, 2, 3, 1, 4]))