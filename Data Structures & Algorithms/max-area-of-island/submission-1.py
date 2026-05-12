class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nR, nC = dr + row, dc + col
                    if 0 <= nR < rows and 0 <= nC < cols and grid[nR][nC] == 1:
                        grid[nR][nC] = 0
                        q.append((nR, nC))
                        res += 1
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        
        return area