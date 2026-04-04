class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Approach
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # Min-Heap Approach
        # freq = {}
        # nums.sort()
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        
        # heap = []
        # for num, count in freq.items():
        #     heapq.heappush(heap, (count, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # ans = []
        # for i in range(k):
        #     ans.append(heapq.heappop(heap)[1])
        
        # return ans