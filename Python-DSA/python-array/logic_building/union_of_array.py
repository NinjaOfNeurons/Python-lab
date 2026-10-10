def check_if_element_is_present(nums3,nums1,i):
    return not nums3 or nums3[-1] != nums1[i]  # nums3[-1] means last element of array 
                                               # not nums3 return True or false base upon if list is empty or not

def union_ary(nums1, nums2):
    i = 0
    j = 0
    nums3 = [] 
    while(i < len(nums1) and  j < len(nums2) ):
        if nums1[i] == nums2[j]:
            if check_if_element_is_present(nums3,nums1,i):
                nums3.append(nums1[i])
            i += 1
            j += 1
        else:
            if nums1[i] < nums2[j]:
                if check_if_element_is_present(nums3,nums1,i):
                    nums3.append(nums1[i])
                i += 1
            else:
                if check_if_element_is_present(nums3,nums2,j):
                    nums3.append(nums2[j])
                j += 1


    # done with 2 pointer now flussing all remaning element to new array nums3
    
    while i< len(nums1):
        if check_if_element_is_present(nums3,nums1,i):
            nums3.append(nums1[i])
        i += 1


    while j< len(nums2):
        if check_if_element_is_present(nums3,nums2,j):
            nums3.append(nums2[j])
        j += 1
    return nums3


print(union_ary( nums1 = [1,1, 2, 3, 4, 5], nums2 = [2,3,4,4,5,6,6]))
