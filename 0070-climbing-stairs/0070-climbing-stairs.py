class Solution:
    def climbStairs(self, n: int) -> int:

    # ============================================================
    # APPROACH 1: TOP-DOWN DP (RECURSION + MEMOIZATION)
    # ============================================================
    #
    # Core idea:
    # At every stair, I have 2 choices:
    #   1. Take 1 step
    #   2. Take 2 steps
    #
    # STATE:
    #   dfs(i) = number of ways to reach stair n
    #            starting from stair i
    #
    # Therefore:
    #   dfs(i) = dfs(i + 1) + dfs(i + 2)
    #
    # BASE CASES:
    #   i == n  -> We reached the destination -> 1 valid way
    #   i > n   -> We went past the destination -> 0 valid ways
    #
    # MEMOIZATION:
    #   Different recursive paths can reach the same stair.
    #   Instead of calculating dfs(i) again, save its answer in cache.
    #
    # TIME:  O(n)
    # SPACE: O(n) for cache + O(n) recursion stack
    # ============================================================

        # cache[i] = answer to dfs(i)
        #
        # -1 means:
        # "We haven't calculated dfs(i) yet."
        cache = [-1] * (n + 1)

        def dfs(i):

            # We reached exactly stair n.
            #
            # There is 1 valid way to finish:
            # STOP.
            # Base case
            if i == n:
                return 1

            # We went past stair n.
            #
            # This is not a valid way, so return 0.
            # Base case
            if i > n:
                return 0

            # If we already calculated dfs(i),
            # don't calculate it again.
            if cache[i] != -1:
                return cache[i]

            # We have 2 choices:
            #
            # Take 1 step -> dfs(i + 1)
            # Take 2 steps -> dfs(i + 2)
            #
            # Total ways = ways from both choices
            # Solving smaller problems
            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]

        # Start at stair 0.
        return dfs(0)


    # ============================================================
    # APPROACH 2: BOTTOM-UP DP (TABULATION)
    # ============================================================
    #
    # Instead of starting at stair 0 and recursively going forward,
    # we start with the smallest known answers and build upward.
    #
    # STATE:
    #   dp[i] = number of ways to REACH stair i
    #
    # IMPORTANT:
    # This state is slightly different from the top-down state.
    #
    # Top-down:
    #   dfs(i) = ways to reach n FROM i
    #
    # Bottom-up:
    #   dp[i] = ways to reach i FROM 0
    #
    # BASE CASES:
    #
    #   dp[0] = 1
    #
    #   There is 1 way to be at stair 0:
    #   Take no steps.
    #
    #   dp[1] = 1
    #
    #   There is 1 way to reach stair 1:
    #   1 step.
    #
    # TRANSITION:
    #
    # To reach stair i, we could have come from:
    #
    #   i - 1  -> take 1 step
    #   i - 2  -> take 2 steps
    #
    # Therefore:
    #
    #   dp[i] = dp[i - 1] + dp[i - 2]
    #
    # TIME:  O(n)
    # SPACE: O(n)
    # ============================================================

        # # dp[i] = number of ways to reach stair i
        # dp = [0] * (n + 1)

        # # Base cases
        # dp[0] = 1
        # dp[1] = 1

        # # Build the answer from smaller subproblems.
        # for i in range(2, n + 1):

        #     # Reach i from:
        #     #
        #     # i - 1 by taking 1 step
        #     # i - 2 by taking 2 steps
        #     #
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]