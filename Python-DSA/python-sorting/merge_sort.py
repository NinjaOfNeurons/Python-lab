def conquer(nums, low,mid, high):
    temp = []
    left, right = low , mid+1
    #two pointer "9", 14<-mid  |  "15"<-mid+1 , 12
    # temp.append(9) then left+1  will be  14 
    while(left <= mid and right <= high):
        if(nums[left] < nums[right]):
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right +=1 

    #if we are done with append logic and few element is still in array then simply append them untill array compeletly empty 
    while(left<=mid):
        temp.append(nums[left])
        left += 1

    while(right<=high):
            temp.append(nums[right])
            right += 1


    #merging back the sorted array simply copy pasting the tempt to orignal array
    k = 0
    while(low <= high):
        nums[low] = temp[k]
        k +=1
        low += 1
    # print(nums)
    

def divide_nums(nums, start, end):
    mid =  (start+end) // 2
    if(start >= end):
        return
    divide_nums(nums, start, mid)
    divide_nums(nums, mid+1, end)
    conquer(nums,start ,mid,end)
    # print(nums)




nums = [9, 14, 15, 12, 6, 8]
divide_nums(nums,0,len(nums)-1)
print(nums)