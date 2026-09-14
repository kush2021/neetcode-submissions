class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                best = max(best, profit)
        return best