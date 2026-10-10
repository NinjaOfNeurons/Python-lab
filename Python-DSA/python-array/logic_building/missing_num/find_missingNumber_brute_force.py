def missing_num_brute_frc(nums):

    for i in range(0,len(nums)+1):
        for j in range(len(nums)):
            if i == nums[j]:
                break
            elif j == len(nums) - 1 and i != nums[j]:
                return i
                

print( missing_num_brute_frc(nums =  [0, 2, 1, 3]))
