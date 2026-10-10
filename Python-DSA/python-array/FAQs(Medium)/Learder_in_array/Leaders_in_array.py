def leaders(nums):

    """
    Find all leaders in an array.

    Python's for-else rule:
    - The 'else' belongs to the 'for' loop, not the 'if'.
    - The 'else' block executes if the loop finishes normally
      without encountering a 'break'.
    - If 'break' executes, the 'else' block is skipped.

    Here, if nums[i] <= nums[j], a greater or equal element
    exists to the right, so we break and reject nums[i].
    If the inner loop finishes without breaking, nums[i]
    is a leader and is appended to the result.
    """
        
    nums3 = []
    for i in range(len(nums)):
    
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:
                break 
        else:
            nums3.append(nums[i])

    return nums3



nums = [1, 2, 5, 3, 1, 2] #5 3 2
print(leaders(nums))


