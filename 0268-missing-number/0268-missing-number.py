class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = [i for i in range(len(nums) + 1)]
        
        for i in range(len(nums) + 1):
            if numbers[i] not in nums:
                return i
        
        return -1