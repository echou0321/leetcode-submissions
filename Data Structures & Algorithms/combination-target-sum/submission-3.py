class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        def dfs(i, total, combo):
            if total == target:
                res.append(combo.copy())
                return
            if i == len(nums) or total > target:
                return 
            combo.append(nums[i])
            dfs(i, total + nums[i], combo)

            combo.pop()
            dfs(i + 1, total, combo)
        dfs(0, 0, combo)
        return res
