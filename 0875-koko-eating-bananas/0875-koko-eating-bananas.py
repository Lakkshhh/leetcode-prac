class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low_speed, high_speed = 1, max(piles)
        min_valid_speed = high_speed
        while low_speed <= high_speed:
            candidate_speed = (low_speed + high_speed) // 2
            total_hours_needed = 0
            for pile in piles:
                total_hours_needed += math.ceil(float(pile) / candidate_speed)
            if total_hours_needed <= h:
                min_valid_speed = candidate_speed
                high_speed = candidate_speed - 1
            else:
                low_speed = candidate_speed + 1
        return min_valid_speed

"""Checking every possible speed starting from 1 upward and simulating hours needed at each would work, but it re-tests speeds one at a time with no way to skip ahead — the key realization is that 'hours needed' is monotonically non-increasing as speed increases, so this has the same shape as Arrange Coins: a monotonic 'does this candidate work' relationship over a range of candidate values, which is the binary-search-on-the-answer trigger. So instead of searching the piles directly, I binary search over possible eating speeds from 1 to max(piles), and for each candidate speed I simulate the total hours required across all piles using ceiling division (since a partial pile still costs a full hour), narrowing toward the smallest speed where total hours stays within h. I chose binary search over linear speed-by-speed simulation because linear search is O(max(piles) · n) in the worst case, whereas binary search only tests O(log(max(piles))) candidate speeds, each costing O(n) to evaluate — I also considered whether a closed-form formula could avoid simulation entirely, but rejected it since the relationship between speed and total hours across uneven pile sizes doesn't reduce to a clean formula the way triangular numbers did in Arrange Coins, so simulation-per-candidate is necessary here. This runs in O(n log(max(piles))) time, since each of the O(log(max(piles))) binary search steps requires an O(n) pass over all piles to compute total hours, and O(1) extra space, since only a few running variables are tracked regardless of input size."""