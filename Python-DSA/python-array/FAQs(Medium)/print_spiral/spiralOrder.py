def spiralOrder(nums):
    row_size = len(nums)
    col_size = len(nums[0])

    top = 0
    left = 0
    down = row_size -1
    right = col_size -1
    ans = []

    # move left to right in above row 
    while top <= down and left <= right:

        if top <= down:
            for row in range(left,right+1):
                ans.append(nums[top][row])
                # print(nums[top][row])
            
            top += 1

        if left <= right:
            for col in range(top, down+1):
                ans.append(nums[col][right])

                # print(nums[col][right])

            right -= 1
        
        for row in range(right, left-1,-1):
            ans.append(nums[down][row])

            # print(nums[down][row])
        down -= 1
        for col in range(down,top -1 , -1 ):
            ans.append(nums[col][left])

            # print(nums[col][left])
        left += 1

    return ans


print(spiralOrder([[1, 2, 3, 4],
                   [5, 6, 7, 8]]))