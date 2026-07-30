class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(total, i, combo):
            if total == target:
                res.append(combo.copy())
                return
            if total > target or i == len(candidates):
                return
            
            combo.append(candidates[i])
            dfs(total + candidates[i], i + 1, combo)
            combo.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(total, i + 1, combo)
        dfs(0, 0, [])
        return res