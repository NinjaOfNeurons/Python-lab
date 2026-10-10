def remove_dups(nums):
    nums3 = []

    for num in nums:
        if not nums3 or nums3[-1] != num:
            nums3.append(num)

    return nums3


nums = [0, 0, 3, 3, 5, 6]
print(remove_dups(nums))