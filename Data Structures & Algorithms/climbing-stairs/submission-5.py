class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(i, dp):
            if i in dp:
                return dp[i]
            if i == 0 or i == 1:
                return 1
            if i < 0:
                return 0
            dp[i] = dfs(i - 1, dp) + dfs(i - 2, dp)
            return dp[i]
        return dfs(n, dp)
            

