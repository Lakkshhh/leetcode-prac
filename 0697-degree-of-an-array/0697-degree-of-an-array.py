class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)
        
        degree = max([len(i) for i in indices.values()])
        best = len(nums)
        for i in indices.values():
            if len(i) == degree:
                best = min(best, i[-1] - i[0] + 1)
        
        return best