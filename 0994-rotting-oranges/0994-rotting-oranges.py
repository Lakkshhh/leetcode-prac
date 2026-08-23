class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = collections.deque()
        fresh_orange_count = 0
        minutes_elapsed = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_orange_count += 1
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh_orange_count > 0 and rotten_queue:
            current_wave_size = len(rotten_queue)
            for i in range(current_wave_size):
                r, c = rotten_queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        rotten_queue.append((row, col))
                        fresh_orange_count -= 1
            minutes_elapsed += 1
        return minutes_elapsed if fresh_orange_count == 0 else -1

""" Since every rotten orange spreads to its fresh neighbors simultaneously each minute, this is a multi-source BFS problem, not a single-source one — if I only started BFS from one rotten orange at a time, I'd lose the 'all rot in lockstep' timing and get the wrong minute count. So I'll seed the BFS queue with every rotten orange's position up front, and process the queue in complete 'waves' — each full pass through the current queue contents represents exactly one minute, since everything in the queue at the start of a wave rotted at the same time and spreads together. I'll track a running count of fresh oranges so I know when to stop, and decrement it every time a fresh orange turns rotten; when the queue empties, if that count has hit zero, every reachable orange rotted and I return the elapsed minute count, but if fresh oranges remain, they were unreachable — isolated by boundaries or empty cells — so I return -1. I chose BFS with a deque over DFS or repeated grid scanning because BFS naturally expands level-by-level, which maps directly onto 'one wave per minute,' whereas DFS would spread depth-first and require extra bookkeeping to recover timing, and repeatedly rescanning the whole grid each minute would waste work re-checking cells that can't possibly change. This runs in O(m·n) time, since every cell is enqueued and processed at most once, and O(m·n) space in the worst case, since the queue could hold up to every cell in the grid if it started almost entirely rotten. """