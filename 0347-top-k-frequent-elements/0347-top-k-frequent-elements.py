class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Bucket Sort Approach
        num_to_frequency = {}
        buckets_by_frequency = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            num_to_frequency[num] = 1 + num_to_frequency.get(num, 0)

        for num, frequency in num_to_frequency.items():
            buckets_by_frequency[frequency].append(num)

        top_k_frequent = []
        for frequency in range(len(buckets_by_frequency) - 1, 0, -1):
            for num in buckets_by_frequency[frequency]:
                top_k_frequent.append(num)
                if len(top_k_frequent) == k:
                    return top_k_frequent

        # Alternate Min-Heap Approach - O(n log k) approach
        # num_to_frequency = {}
        # for num in nums:
        #     num_to_frequency[num] = num_to_frequency.get(num, 0) + 1
        #
        # min_heap = []
        # for num, frequency in num_to_frequency.items():
        #     heapq.heappush(min_heap, (frequency, num))
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        #
        # top_k_frequent = []
        # for i in range(k):
        #     top_k_frequent.append(heapq.heappop(min_heap)[1])
        #
        # return top_k_frequent


"""Sorting all distinct elements by frequency would work but costs O(n log n) and sorts more than I actually need, since I only care about the top k, not a full ranking — the key realization is that frequency itself is bounded by n (an element can appear at most len(nums) times), which means I can use frequency as a direct array index instead of comparing and sorting: I build buckets where buckets_by_frequency[f] holds every number that appears exactly f times, then walk the buckets from highest frequency down, collecting numbers until I have k. I chose bucket sort over a min-heap of size k — which I considered and left in as a named alternative — because bucket sort achieves true O(n) time by exploiting the bounded frequency range as an indexing trick, whereas the heap approach costs O(n log k) since every insertion/eviction is a log-time heap operation; the heap version is still a reasonable choice if frequency weren't cleanly bounded by n, or if a streaming/online version of this problem were asked instead of a single batch computation. This runs in O(n) time, since building the frequency map and buckets is a single linear pass and the final bucket walk visits at most n total elements across all buckets, and O(n) space for the frequency map and bucket array, both sized relative to the input."""