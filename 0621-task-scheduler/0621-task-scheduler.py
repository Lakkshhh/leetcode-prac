class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # aim is to minimize the idle tnme
        count = {}
        for i in range(len(tasks)):
            count[tasks[i]] = 1 + count.get(tasks[i], 0)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() # pairs of [-cnt, idleTime]
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # we add one since they are being stored as negative values
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time