class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        min_price = prices[left]

        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1
            else :
                if prices[right] < min_price:
                    min_price = prices[right]
                    left = right
                right += 1

        return max_profit
