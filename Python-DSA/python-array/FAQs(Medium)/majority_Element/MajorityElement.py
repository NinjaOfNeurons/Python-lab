def majority_element(nums):
    freq = {    }
    criteria = len(nums) // 2
    for num in nums:
        freq[num] = freq.get(num,0) + 1

    for k,v in freq.items():
        if v > criteria:
            return k

nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

print(majority_element(nums))

    
    
    
    
    
    
    
    





    