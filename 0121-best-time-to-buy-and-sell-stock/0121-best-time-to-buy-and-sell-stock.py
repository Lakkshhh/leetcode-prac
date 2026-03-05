class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Dynamic Approach:

        max_p = 0
        min_buy = prices[0]

        for sell in prices:
            max_p = max(max_p, sell - min_buy)
            min_buy = min(min_buy, sell)
        
        return max_p

        #Two Pointer Approach

        # left, right = 0, 1
        # max_p = 0

        # while right < len(prices):
        #     if prices[right] > prices[left]:
        #         max_profit = max(max_p, prices[right] - prices[left])
        #     else :
        #         left = right
        
        #     right += 1

        # return max_p
