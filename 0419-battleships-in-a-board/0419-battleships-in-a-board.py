class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Idea is that each ship's starting point has "." above it and left of it, so it is easy to track a whole ship just using that when traversing through entire grid

        count = 0

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "X":
                    if (i == 0 or board[i - 1][j] == ".") and\
                       (j == 0 or board[i][j - 1] == "."):
                            count += 1
                            
        return count

        # BFS Approach, can be done in DFS as well using recursion
        # rows, cols = len(board), len(board[0])
        # visited = set()
        # islands = 0
        # if not board:
        #     return 0

        # def bfs(i, j):
        #     queue = collections.deque()
        #     visited.add((i, j))
        #     queue.append((i, j))
        #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        #     while queue:
        #         row, col = queue.popleft()
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if r in range(rows) and c in range(cols) and (r, c) not in visited and board[r][c] == "X":
        #                 visited.add((r, c))
        #                 queue.append((r, c))

        # for i in range(rows):
        #     for j in range(cols):
        #         if board[i][j] == "X" and (i, j) not in visited:
        #             bfs(i, j)
        #             islands += 1
        # return islands