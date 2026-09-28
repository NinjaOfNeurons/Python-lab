def second_highest(nums):
    freq = {}
    k=2
    for num in nums:
        freq[num] = freq.get(num, 0) + 1


    sorted_freq = sorted(
        freq.items(),  #gives pairs: (1, 1) (2, 4)
        key=lambda x: x[1], # "Sort using the second thing in each pair."
        reverse=True) #largest → 

    
    print(sorted_freq)

    return sorted_freq[k - 1][0]    # (2nd -1) means 0,"1"  and 1 value of pair 


print(second_highest([1,2,3,2,2,4,3,2,]))