class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = {}

        for i, n in enumerate(numbers):
            ans[n] = i
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in ans:
                return [i+1, ans[diff]+1]
                
        return []