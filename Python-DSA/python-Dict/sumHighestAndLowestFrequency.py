def sumHighestAndLowestFrequency(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    sorted_pairs = sorted(freq.items(),
                        key = lambda x:x[1],
                        reverse=True )
    print(sorted_pairs)
    print( sorted_pairs[0][1] , sorted_pairs[len(sorted_pairs) -1][1])

    sum  =   sorted_pairs[0][1] + sorted_pairs[len(sorted_pairs) -1][1]

    return(sum)
print(sumHighestAndLowestFrequency([1,2,2,3,3,3,4,3,]))
