class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i, n in enumerate(nums):
            ans[n] = i

        for i, n in  enumerate(nums):
            diff = target - n
            if diff in ans and ans[diff] != i:
                return [i, ans[diff]]

        return []