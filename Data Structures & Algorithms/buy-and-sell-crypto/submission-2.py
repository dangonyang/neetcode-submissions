class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            sell = prices[i]
            if sell < buy:
                buy = sell
            profit = max(profit, sell - buy)
        return profit