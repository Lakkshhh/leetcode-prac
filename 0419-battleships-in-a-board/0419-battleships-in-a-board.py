class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        visited = []
        islands = 0
        if not board:
            return 0

        def bfs(i, j):
            queue = collections.deque()
            visited.append((i, j))
            queue.append((i, j))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visited and board[r][c] == "X":
                        visited.append((r, c))
                        queue.append((r, c))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
