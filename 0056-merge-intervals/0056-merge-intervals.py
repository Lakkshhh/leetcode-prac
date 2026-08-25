class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda pair: pair[0])
        merged_intervals = [intervals[0]]

        for start, end in intervals:
            last_merged_end = merged_intervals[-1][1]

            if start <= last_merged_end:
                merged_intervals[-1][1] = max(last_merged_end, end) # max cause edge case [[1, 5], [2, 4]]
            else:
                merged_intervals.append([start, end])
        return merged_intervals


"""Overlap between two intervals is easy to check when they're adjacent to each other, but intervals can arrive in any order, so I first sort by start time — that guarantees that if interval A doesn't overlap the interval immediately before it, it can't overlap anything even earlier either, since everything before A started even sooner. Once sorted, I only ever need to compare each interval against the last interval I've already merged: if the current interval's start is within (or touching) the last merged interval's end, they overlap and I extend that last interval's end to cover both; otherwise, the current interval starts a genuinely new group. I chose sort-then-linear-scan over something like an interval tree or repeatedly re-scanning all intervals for overlaps because sorting reduces the problem to comparing only consecutive intervals rather than checking every pair, and a single linear pass after sorting is sufficient since overlap can only ever propagate forward once intervals are ordered by start time — an interval tree would be overkill here since I only need one merge pass over a static input, not repeated dynamic range queries. This runs in O(n log n) time, dominated by the initial sort, since the linear scan afterward is O(n), and O(n) space for the sorted output list in the worst case where no intervals overlap at all."""