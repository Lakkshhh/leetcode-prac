class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_sum = 0

        for num in nums:
            max_sum = max(max_sum + num, num)
            res = max(res, max_sum)

        return res