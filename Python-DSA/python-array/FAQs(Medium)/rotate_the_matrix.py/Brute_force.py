
def rotate_mat_90(nums):
    row_size = len(nums)
    col_size = len(nums[0])

    ans = []

    for col in range(col_size):
        row_ans = []

        for row in range(row_size - 1, -1, -1):
            print(row,col,nums[row][col])
            row_ans.append(nums[row][col])

        ans.append(row_ans)

    return ans


nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_mat_90(nums))
