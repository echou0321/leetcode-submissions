class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def dfs(m, n, dp):
            if (m, n) in dp:
                return dp[m, n]
            if m == 1 and n == 1:
                return 1
            if m == 0 or n == 0:
                return 0
            dp[m, n] = dfs(m - 1, n, dp) + dfs(m, n - 1, dp)
            return dp[m, n]

        return dfs(m, n, dp)