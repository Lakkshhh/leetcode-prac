class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # index
        l = r = 0

        while r < len(nums):
            # pop smaller values from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            # append max value when window is correct size
            if r + 1 >= k:
                res.append(nums[q[0]]) # it's a monotonically decreasing queue
                l += 1
            r += 1
        
        return res

        # Brute Force:

        # res = []
        # l = 0
        # for r in range(k - 1, len(nums)):
        #     c = max(nums[l : r + 1])
        #     res.append(c)
        #     l += 1
        
        # return res