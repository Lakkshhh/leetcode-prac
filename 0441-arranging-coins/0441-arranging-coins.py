class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid_rows_built = low + (high - low) // 2
            coins_required = mid_rows_built * (mid_rows_built + 1) // 2
            if coins_required == n:
                return mid_rows_built
            elif coins_required < n:
                low = mid_rows_built + 1
            else:
                high = mid_rows_built - 1
        return high


"""The number of coins needed to build k complete rows grows monotonically as k increases — it's k(k+1)/2, a strictly increasing function — and monotonic 'does this candidate value work or not' relationships are exactly the trigger for binary search on the answer, rather than simulating row-by-row construction. 
Sum of first k natural numbers: k∗(k+1)/2.
So we want the largest k satisfying k∗(k+1)/2≤n.
Binary search is perfect for this, it guesses the number of rows, checks how many coins those rows need, and moves left or right until it finds the maximum number of rows that can be completely built.
So instead of literally building rows one at a time and subtracting coins until I run out, I binary search over the possible number of complete rows, computing how many coins a candidate row count would require via the closed-form triangular number formula, and narrowing the search range based on whether that candidate uses too many, too few, or exactly n coins. I chose binary search over linear simulation because simulation would take O(√n) time anyway in the best informal implementations, but binary search gets me to O(log n) cleanly and more importantly demonstrates the monotonicity insight directly rather than discovering it by brute iteration; I also considered directly solving the quadratic k(k+1)/2 = n via the quadratic formula for O(1) time, but rejected it here since floating-point precision on the square root could introduce off-by-one errors near exact boundaries, whereas binary search stays exact using only integer arithmetic. This runs in O(log n) time, since the search range for k shrinks by half each iteration, and O(1) space, since only a few integer variables are tracked throughout.""" 