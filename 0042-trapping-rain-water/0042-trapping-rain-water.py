class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        max_area = 0

        if len(height) <= 2:
            return 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                max_l = max(max_l, height[l])
                max_area += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                max_area += max_r - height[r]

        return max_area

        
        # l, r = 0, len(height) - 1
        # max_l, max_r = height[l], height[r]
        # max_area = 0

        # if len(height) <= 2:
        #     return 0

        # while l < r:
        #     if height[l] <= height[r]:
        #         if max_l <= height[l]:
        #             max_l = height[l]
        #         else:
        #             max_area += max_l - height[l]
        #         l += 1
        #     else:
        #         if max_r <= height[r]:
        #             max_r = height[r]
        #         else:
        #             max_area += max_r - height[r]
        #         r -= 1

        # return max_area
