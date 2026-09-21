def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(nums):
    for i in range(len(nums)):
        min_val = nums[i]
        min_j_index = i

        for j in range(i + 1, len(nums)):
            if min_val > nums[j]:
                min_val = nums[j]
                min_j_index = j

        swap(nums, i, min_j_index)

    return nums


print(selection_sort([7, 5, 9, 2, 8]))