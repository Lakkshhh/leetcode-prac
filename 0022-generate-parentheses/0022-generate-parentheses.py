class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pair = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(pair))
                return
            
            if open < n:
                pair.append("(")
                backtrack(open + 1, closed)
                pair.pop()
            
            if closed < open:
                pair.append(")")
                backtrack(open, closed + 1)
                pair.pop()
        
        backtrack(0, 0)
        return res