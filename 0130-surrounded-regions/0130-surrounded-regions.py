class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])

        def mark_safe_from_border(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "SAFE"
            mark_safe_from_border(r + 1, c)
            mark_safe_from_border(r - 1, c)
            mark_safe_from_border(r, c + 1)
            mark_safe_from_border(r, c - 1)

        # (DFS) Capturing unsurrounded regions in first and last column (O -> SAFE)
        for r in range(ROWS):
            if board[r][0] == "O":
                mark_safe_from_border(r, 0)
            if board[r][COLS - 1] == "O":
                mark_safe_from_border(r, COLS - 1)

        # (DFS) Capturing unsurrounded regions in first and last row (O -> SAFE)
        for c in range(COLS):
            if board[0][c] == "O":
                mark_safe_from_border(0, c)
            if board[ROWS - 1][c] == "O":
                mark_safe_from_border(ROWS - 1, c)

        # Capturing surrounded regions (O -> X) and then uncapturing unsurrounded regions (SAFE -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "SAFE":
                    board[r][c] = "O"


"""Trying to detect 'surrounded' directly by checking, for every 'O', whether its whole connected region ever touches the border would mean repeatedly re-exploring the same connected components from scratch for every cell in them, wasting work — so instead I flip it, same as Pacific Atlantic: start DFS only from the border 'O' cells, since those are the only cells that can possibly be safe, and mark everything reachable from them as temporarily protected. Anything left as a plain 'O' after that traversal was never connected to the border, so it's genuinely surrounded and gets flipped to 'X', while everything I marked as safe gets flipped back to 'O'. I chose DFS from the border inward over checking each region's border-adjacency individually because the border-outward approach guarantees each cell is visited and classified exactly once, rather than re-verifying region membership repeatedly, and I used in-place placeholder marking (a third character) instead of a separate visited set because the board itself can double as the visited-state tracker, avoiding extra space for a lookup structure. This runs in O(m·n) time, since every cell is visited a constant number of times across the border DFS and the final sweep, and O(m·n) space in the worst case for the recursion stack if the entire board is one connected region of 'O's."""