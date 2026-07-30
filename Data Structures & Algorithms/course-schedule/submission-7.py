class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        seen = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            
            seen.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) is False:
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if dfs(crs) is False:
                return False
        return True