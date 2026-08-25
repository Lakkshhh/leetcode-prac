class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left_pointer, right_pointer = 0, len(height) - 1
        left_max, right_max = height[left_pointer], height[right_pointer]
        trapped_water = 0
        while left_pointer < right_pointer:
            if left_max < right_max:
                left_pointer += 1
                left_max = max(left_max, height[left_pointer])
                trapped_water += left_max - height[left_pointer]
            else:
                right_pointer -= 1
                right_max = max(right_max, height[right_pointer])
                trapped_water += right_max - height[right_pointer]
        return trapped_water


"""The brute-force way to compute water at each index is to separately scan left and scan right from that index to find the tallest bar in each direction, but that's redundant work repeated at every single index — the key realization is that I don't need the exact max on both sides at every point, I only need to know which side's max is smaller, since that smaller max is what actually bounds the trapped water at the current position. That lets me use two pointers starting from both ends, always advancing whichever side currently has the smaller running max — because if the left max is smaller than the right max, I know for certain that the true right-side max (even parts I haven't scanned yet) can only be greater than or equal to what I've already seen, so the left max alone safely determines the trapped water at the left pointer's position without needing to know the exact right max. I chose two pointers over precomputing full left-max and right-max arrays because both give O(n) time, but two pointers does it in O(1) space by only tracking a single running max per side instead of storing a max value at every index; I also considered a monotonic stack, which processes bars in horizontal 'layers' and is a valid alternative, but it's more natural for the related 'largest rectangle' style problems and adds bookkeeping complexity here that two pointers avoids entirely. This runs in O(n) time, since each pointer moves inward exactly once across the whole traversal, and O(1) space, since I only track a handful of running variables regardless of input size."""