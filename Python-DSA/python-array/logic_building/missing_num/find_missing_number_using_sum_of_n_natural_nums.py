def missingNumber_sum_of_n_nums(nums):
    n = len(nums) 
    n_sum = n * (n+1) // 2 # if values is exactly 1 then find the sum of n natural numbers 
                            # then sum your array then diffrence of both is your answer 

    ary_sum = 0

    for num in nums:
        ary_sum = ary_sum + num

    return n_sum  -  ary_sum
      
print(missingNumber_sum_of_n_nums( [3, 2, 1, 4]))