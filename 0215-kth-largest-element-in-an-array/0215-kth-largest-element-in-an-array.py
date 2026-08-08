class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Heap solution
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]

        # Quickselect solution (due to it's better O(n) average case)

        # k = len(nums) - k

        # def quickSelect(l, r):
        #     pivot_index = random.randint(l, r)
        #     nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
        #     pivot, p = nums[r], l

        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1 
        #     nums[p], nums[r] = nums[r], nums[p]
            
        #     if p > k:
        #         return quickSelect(l, p - 1)
        #     elif p < k:
        #         return quickSelect(p + 1, r)
        #     else:
        #         return nums[p]
        
        # return quickSelect(0, len(nums) - 1)