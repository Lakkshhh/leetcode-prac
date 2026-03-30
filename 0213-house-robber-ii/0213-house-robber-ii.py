class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        
        return dfs(0)

        # Bottom Up Dynamic Programming Approach

        # if len(nums) == 1:
        #     return nums[0]
        # return max(self.helper(nums[1:]),
        #            self.helper(nums[:-1]))

        # def helper(self, nums: List[int]) -> int:
        #     if not nums:
        #         return 0
        #     if len(nums) == 1:
        #         return nums[0]

        #     dp = [0] * len(nums)
        #     dp[0] = nums[0]
        #     dp[1] = max(nums[0], nums[1])

        #     for i in range(2, len(nums)):
        #         dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        #     return dp[-1]


        # Space Optimized Approach

        # return max(nums[0], self.helper(nums[1:]),
        #                     self.helper(nums[:-1]))

        # def helper(self, nums):
        #     rob1, rob2 = 0, 0

        #     for num in nums:
        #         newRob = max(rob1 + num, rob2)
        #         rob1 = rob2
        #         rob2 = newRob
        #     return rob2