class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0

        def bfs(start_row, start_col):
            queue = deque()
            grid[start_row][start_col] = "0"
            queue.append((start_row, start_col))
            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in directions:
                    next_row, next_col = row + delta_row, col + delta_col
                    if (next_row < 0 or next_col < 0 or next_row >= ROWS or
                        next_col >= COLS or grid[next_row][next_col] == "0"
                    ):
                        continue
                    queue.append((next_row, next_col))
                    grid[next_row][next_col] = "0"

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    island_count += 1
        return island_count


"""Counting islands means counting connected components of '1's in the grid, where connectivity is 4-directional — so this is a graph traversal problem where each land cell is a node and adjacency comes from grid neighbors rather than an explicit edge list. I scan every cell, and whenever I find an unvisited '1', that's a brand new island, so I increment the count and then flood-fill outward from it, marking every connected land cell as visited (by overwriting to '0') so it's never counted again as the start of a new island. I chose BFS with a queue over DFS with recursion because BFS avoids Python's recursion depth limit on large, snake-like connected islands, and I mutate the grid in place to mark visited cells rather than using a separate visited set, trading the ability to preserve the original grid for saving the O(rows·cols) space a separate visited structure would otherwise cost. This runs in O(rows · cols) time, since every cell is visited and processed at most once across all BFS calls combined, and O(min(rows, cols)) space in the worst case for the BFS queue, since the frontier of a flood fill can't exceed the shorter grid dimension at any point in time.

Let me first make sure I understand the problem: I've got a grid of 1s and 0s where 1 represents land and 0 represents water, and I need to count how many separate islands there are, where an island is just a group of 1s connected horizontally or vertically. The key observation is that this is really a connected components problem — once I land on an unvisited piece of land, I know every piece of land touching it, directly or indirectly, belongs to the same island, so I just need a way to explore an entire connected chunk of land at once and make sure I don't count it again. That makes me think of a grid traversal like BFS or DFS, and I lean toward BFS with a queue here, since it lets me flood-fill outward from a starting cell without recursion depth being a concern on a large grid. So the approach is: I scan through every cell in the grid, and whenever I hit a cell that's land, I know I've found a new island, so I bump my island count and kick off a BFS from that cell to mark every connected piece of land as visited; inside the BFS, I use a queue starting with that cell, and I immediately mark it as visited by flipping it to "0" so I don't run into it again later, then for each cell I pop off the queue, I check its four neighbors, and as long as a neighbor is in bounds and is still land, I add it to the queue and immediately mark it visited too. One implementation detail I'd call out is that I mark cells as visited right when I add them to the queue rather than when I pop them, which avoids adding the same cell to the queue multiple times before it's processed. Since I'm mutating the grid in place to track visited cells, I don't need a separate visited set, which keeps the space usage down, though if I weren't allowed to modify the input I'd just swap that flag for a visited set instead. In terms of complexity, this is O(rows times cols) time, since every cell gets visited and enqueued at most once across all the BFS calls combined, and space is O(rows times cols) in the worst case too, for the queue if the entire grid turns out to be one giant island."""