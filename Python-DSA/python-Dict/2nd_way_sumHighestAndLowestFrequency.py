def sumHighestAndLowestFrequency(nums):

    freq = {}

    # 1. Build frequency map
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # 2. Track highest and lowest
    highest = 0
    lowest = float('inf')   #highest number ever  exist in float 

    # 3. Scan frequencies
    for count in freq.values():
        highest = max(highest, count)
        lowest = min(lowest, count)

    return highest + lowest