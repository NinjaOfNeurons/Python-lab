def max_ones(nums):
    count = 0 
    max_count = 0
    for num in nums:
        # print(num)
        if num  == 1:
            count  += 1
            if count > max_count:
                max_count = count
            # print("one")
        else:
            count = 0
    return max_count

print(max_ones([1, 1, 0, 0, 1, 1, 1, 1]))