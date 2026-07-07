class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canBuy):
            if (i, canBuy) in dp:
                return dp[i, canBuy]
            if i >= len(prices):
                return 0
            if canBuy:
                buy = dfs(i + 1, not canBuy) - prices[i]
                skip = dfs(i + 1, canBuy)
                dp[i, canBuy] = max(buy, skip)
            else:
                sell = dfs(i + 2, not canBuy) + prices[i]
                skip = dfs(i + 1, canBuy)
                dp[i, canBuy] = max(sell, skip)
            return dp[i, canBuy]
        return dfs(0, True)