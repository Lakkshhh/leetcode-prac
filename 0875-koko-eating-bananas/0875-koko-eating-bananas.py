import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            hours = 0
            mid = low + (high - low) // 2

            for i in piles:
                hours += ceil(i / mid)

            if hours <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return res