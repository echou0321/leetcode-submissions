class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        combo = []

        def dfs(i, total, combo):
            if total == target:
                res.append(combo.copy())
                return
            if total > target or i == len(candidates):
                return    
            
            combo.append(candidates[i])
            dfs(i + 1, total + candidates[i], combo)

            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total, combo)
        
        dfs(0, 0, combo)
        return res


        