class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency_counts = Counter(tasks)
        max_frequency = max(task_frequency_counts.values()) 
        max_frequency_label_count = sum(
            1 for frequency in task_frequency_counts.values()
            if frequency == max_frequency
        )

        idle_skeleton_size = (max_frequency - 1) * (n + 1) + max_frequency_label_count

        return max(len(tasks), idle_skeleton_size)
        
        # aim is to minimize the idle time

        # count = {}
        # for i in range(len(tasks)):
        #     count[tasks[i]] = 1 + count.get(tasks[i], 0)
        # maxHeap = [-i for i in count.values()]
        # heapq.heapify(maxHeap)

        # time = 0
        # queue = deque() # pairs of [-cnt, idleTime]
        # while maxHeap or queue:
        #     time += 1
        #     if maxHeap:
        #         cnt = 1 + heapq.heappop(maxHeap) # we add one since they are being stored as negative values
        #         if cnt:
        #             queue.append([cnt, time + n])
        #     if queue and queue[0][1] == time:
        #         heapq.heappush(maxHeap, queue.popleft()[0])
        
        # return time