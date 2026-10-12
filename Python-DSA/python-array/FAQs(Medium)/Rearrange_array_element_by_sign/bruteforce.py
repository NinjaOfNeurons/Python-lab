
class Solution:
    def rearrange(self, nums):
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        nums = []
        i = 0
        j = 0

        while i < len(positive) and j < len(negative):
            nums.append(positive[i])
            nums.append(negative[j])
            i += 1
            j += 1

        return nums


    


obj = Solution()
nums = [2, 4, 5, -1, -3, -4]
print(obj.rearrange(nums))
