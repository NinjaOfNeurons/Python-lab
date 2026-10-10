
def intersection(nums1, nums2):
    i = 0
    j = 0
    nums3 = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            nums3.append(nums1[i])
            i += 1
            j += 1
        else:
            if nums1[i]<nums2[j]:
                i += 1
            else:
                j += 1

    return nums3



print(intersection(  nums1 = [1, 2, 2, 3, 3, 3], nums2 = [2, 3, 3, 4, 5, 7]))
