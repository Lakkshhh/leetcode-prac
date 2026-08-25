class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left_pointer, right_pointer = 0, 1
        max_profit = 0

        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                current_profit = prices[right_pointer] - prices[left_pointer]
                max_profit = max(max_profit, current_profit)
            else:
                left_pointer = right_pointer
            right_pointer += 1
        return max_profit


"""Checking every possible buy-sell pair is O(n²), but a lot of that work is wasted — I don't need to compare today's price against every past price individually, I only ever care about the minimum price seen so far, since that's always the best possible buy day up to this point. So I use two pointers: left tracks the current candidate buy day (effectively the lowest price seen so far), and right scans forward as the candidate sell day; if selling at right beats selling at any point I've already recorded, I update the max profit, and if the price at right ever drops below the price at left, left jumps forward to right, since a cheaper buy day just appeared and there's no reason to keep considering the old, worse one. I chose this single-pass two-pointer approach over brute-force pairwise comparison because it collapses O(n²) comparisons into O(n) by exploiting the fact that only the running minimum-so-far ever matters for a future sell, and I also considered this as a Kadane's-algorithm-style DP variant — tracking max profit ending at each day — which is mathematically equivalent and arguably conceptually cleaner, but the pointer-based framing directly mirrors the 'track the best buy day' intuition without extra DP state naming. This runs in O(n) time, since both pointers only ever move forward and each index is visited a constant number of times, and O(1) space, since only a few running variables are tracked regardless of input size."""