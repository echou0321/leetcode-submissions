class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = {}

        def dfs(i, total):
            if (i, total) in dp:
                return dp[i, total]
            if total == 0:
                dp[(i, total)] = True
                return True
            if total < 0 or i >= len(nums):
                dp[i, total] = False
                return False
            dp[i, total] = dfs(i + 1, total - nums[i]) or dfs(i + 1, total)
            return dp[i, total]
        return dfs(0, target)


            



