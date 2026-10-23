def dic_2Sum(nums, target):
    dic_num = {}
    for i , val in enumerate(nums):
        req =  target - val 
        if req  in dic_num:
            return(i,dic_num[req])
        else:
            print(dic_num)
            dic_num[val] = i

            
print(dic_2Sum( nums = [1, 6, 2, 10, 3], target = 13))
