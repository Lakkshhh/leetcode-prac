class MedianFinder:

    import heapq

class MedianFinder:
    def __init__(self):
        # two heaps: lower_half_max_heap, upper_half_min_heap
        # heaps should be equal size (or lower_half at most 1 bigger)
        self.lower_half_max_heap, self.upper_half_min_heap = [], []

    def addNum(self, num: int) -> None:
        if self.upper_half_min_heap and num > self.upper_half_min_heap[0]:
            heapq.heappush(self.upper_half_min_heap, num)
        else:
            heapq.heappush(self.lower_half_max_heap, -1 * num)

        if len(self.lower_half_max_heap) > len(self.upper_half_min_heap) + 1:
            moved_value = -1 * heapq.heappop(self.lower_half_max_heap)
            heapq.heappush(self.upper_half_min_heap, moved_value)
        if len(self.upper_half_min_heap) > len(self.lower_half_max_heap) + 1:
            moved_value = heapq.heappop(self.upper_half_min_heap)
            heapq.heappush(self.lower_half_max_heap, -1 * moved_value)

    def findMedian(self) -> float:
        if len(self.lower_half_max_heap) > len(self.upper_half_min_heap):
            return -1 * self.lower_half_max_heap[0]
        elif len(self.upper_half_min_heap) > len(self.lower_half_max_heap):
            return self.upper_half_min_heap[0]
        return (-1 * self.lower_half_max_heap[0] + self.upper_half_min_heap[0]) / 2.0
        
''' I need fast access to the median of a growing, unordered stream, and the key realization is I never need the whole stream sorted — I only ever need to know what's sitting right at the midpoint. So I'll split the data into two halves: a max-heap holding the smaller half, so its top is the largest value just below the median, and a min-heap holding the larger half, so its top is the smallest value just above the median. I'll keep these two heaps balanced in size — equal, or the lower half at most one bigger — so the median is always either the top of the bigger heap, or the average of both tops when they're equal. On every insert I'll add to one heap, then immediately rebalance if the sizes drift apart by more than one, which keeps every operation at O(log n) for inserts and O(1) for reading the median, since I'm never fully sorting anything — I'm just maintaining the boundary. '''

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()