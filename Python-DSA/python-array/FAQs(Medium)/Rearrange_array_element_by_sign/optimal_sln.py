
class Solution:
    def rearrange(self, nums):
        ans = [0] * len(nums)
        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2

        return ans


obj = Solution()
nums = [2, 4, 5, -1, -3, -4]
print(obj.rearrange(nums))
