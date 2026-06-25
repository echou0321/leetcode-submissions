class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        processed = set()
        cycle = set()
        res = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in processed:
                return True
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            processed.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res

