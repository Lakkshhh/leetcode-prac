class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)
            # Since amount of water depends only on the minimum height, it is appropriate to replace the smaller height value.
            if height[l] <= height[r]: 
                l +=1
            else:
                r -= 1
        
        return max_area