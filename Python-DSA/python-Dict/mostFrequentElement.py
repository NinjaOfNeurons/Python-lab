def mostFrequentElement(nums):
    freq = {}
    for num in nums:
        freq[num] =  freq.get(num,0)+1

    max_freq =0
    answer = 0 
    for num in freq:
        if(freq[num] > max_freq):
            max_freq = freq[num]
            answer = num
        elif freq[num] == max_freq and num < answer:
            answer = num

    # print(num)
    return answer

print(mostFrequentElement([1,2,2,4,6]))