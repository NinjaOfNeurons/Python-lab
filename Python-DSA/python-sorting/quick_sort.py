def partition(nums, low, high):
    """
    1. Pick pivot
    2. Find smaller elements
    3. Keep them on the left
    4. Put pivot in its correct position
    5. Return pivot position
    """

    pivot = nums[high]
    small = low

    for i in range(low,high):
        if nums[i] < pivot:
            nums[i] , nums[small] = nums[small], nums[i]
            small += 1
    nums[small], nums[high] = pivot, nums[small]   #replacing pivot with [3, 2, 8, 5, 6, 7, 4]      now   [3, 2, 4, 5, 6, 7, 8]
                                                                    #        ↑              ↑                    ↑
                                                                    #      small           pivot               pivot
    print(nums,"partition")
    return small   #current pivot value


    

def quick_sort(low, high , nums ):
    if low >= high:
        print(nums)
        return 
    
    pivot_index = partition(nums, low, high)
    quick_sort(low, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, high, nums)



nums = [3, 2, 8, 5, 6, 7, 4]
print(quick_sort( 0, len(nums)-1, nums ))

"""
Partition = rearrange one section around a pivot.
Recursion = keep doing that to the smaller sections until everything is sorted.

"""