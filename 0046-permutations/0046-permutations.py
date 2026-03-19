class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        #Pick a number for position i, explore ALL possibilities, then put it back and try the next number.
        def perm(i):
            if i == len(nums):
                res.append(nums[:])
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perm(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        perm(0)
        return res