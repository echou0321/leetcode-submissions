class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r, = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit