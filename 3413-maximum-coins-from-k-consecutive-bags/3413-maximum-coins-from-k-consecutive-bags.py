class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins_in_window = max_coins = window_start_index = 0
        coins.sort()
        for window_end_index in range(len(coins)):
            segment_start, segment_end, coins_per_bag = coins[window_end_index]
            coins_in_window += coins_per_bag * (segment_end - segment_start + 1)
            while coins[window_end_index][1] - coins[window_start_index][0] > k - 1:
                overflow_bag_count = coins[window_end_index][1] - coins[window_start_index][0] + 1 - k
                max_coins = max(max_coins, coins_in_window - overflow_bag_count * coins_per_bag)
                start_segment_start, start_segment_end, start_segment_coins_per_bag = coins[window_start_index]
                if start_segment_end - start_segment_start + 1 > overflow_bag_count:
                    coins_in_window -= start_segment_coins_per_bag * overflow_bag_count
                    coins[window_start_index][0] += overflow_bag_count
                else:
                    coins_in_window -= start_segment_coins_per_bag * (start_segment_end - start_segment_start + 1)
                    window_start_index += 1
            max_coins = max(max_coins, coins_in_window)
        return max_coins


"""Since coordinates can be enormous but the number of segments is what's actually bounded, I can't slide a window bag-by-bag — I need to think of the window in terms of segments, treating each segment as a bulk unit of (count of bags) × (coins per bag) rather than iterating individual positions, which points toward a two-pointer sliding window over the sorted segment list rather than over raw coordinates. I expand the window by adding segments on the right and accumulating their total coin contribution, and whenever the window's bag span (right segment's end minus left segment's start) exceeds k - 1, I've overshot — so I calculate exactly how many bags of overflow exist at the left edge, check the best answer assuming I trim exactly that overflow off the left, then either partially shrink the leftmost segment (if it has more bags than the overflow) or fully drop it and advance the window's left pointer. I chose a segment-level two-pointer sliding window over a coordinate-level sliding window because the coordinate range can be astronomically large while the segment count is what's actually small and boundable, and treating each segment as one atomic unit of work turns a potentially huge-range problem into one bounded by segment count instead. This runs in O(n log n) time, dominated by the initial sort, since the two-pointer window itself does O(n) amortized work as each segment is added and removed from the window at most once, and O(1) extra space beyond the sort, since the window bookkeeping is just a few running variables and in-place mutation of the segment array."""