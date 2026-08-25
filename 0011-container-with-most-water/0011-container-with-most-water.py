class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left_pointer, right_pointer = 0, len(heights) - 1
        max_area = 0

        while left_pointer < right_pointer:
            current_area = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            max_area = max(max_area, current_area)
            # Since amount of water depends only on the minimum height, it is appropriate to replace the smaller height value
            if heights[left_pointer] <= heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area


"""Brute-force checking every pair of lines gives O(n²), which re-evaluates a lot of pairs that can't possibly beat the current best — the key insight is that starting from the widest possible container (both ends of the array) and always moving the pointer at the shorter line inward is safe, because that shorter line is the bottleneck limiting the current area, and keeping it in place while shrinking width can never produce a better result than what's already been recorded — only moving past it gives any chance of finding a taller line that could increase area despite the reduced width. I chose two pointers over brute-force pairwise comparison because two pointers guarantees each index is visited a constant number of times total, collapsing what would be O(n²) comparisons into O(n); I also considered a stack-based approach akin to the 'largest rectangle in histogram' problem, but rejected it since that pattern solves for a different constraint (maximizing area under a contiguous skyline), whereas here any two lines can pair regardless of what's between them, which is exactly what makes the greedy two-pointer shrink-from-the-shorter-side argument valid. This runs in O(n) time, since the two pointers move toward each other and the loop terminates once they meet, and O(1) space, since only a few running variables are tracked regardless of input size."""