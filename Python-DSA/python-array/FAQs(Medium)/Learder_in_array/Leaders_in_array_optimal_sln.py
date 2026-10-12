# def leaders(nums):
#     nums3 =[]
#     max =  float('-inf')
#     for i in range(len(nums) -1 , -1 , -1):   # reverse loooping array 
#         if nums[i] > max:
#             nums3.append(nums[i])
#             max = nums[i]

#     return nums3

        

def leaders(nums):
    nums3 = []
    max_num = float('-inf')

    for num in reversed(nums):
        if num > max_num:
            nums3.append(num)
            max_num = num

    return nums3[::-1]




nums = [1, 2, 5, 3, 1, 2] #5 3 2
print(leaders(nums))


