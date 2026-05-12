class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        cols, rows = len(grid[0]), len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1
        
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row + dr, col + dc
                    if (newR < 0 or newC < 0 or newR >= rows or
                        newC >= cols or grid[newR][newC] == 0):
                        continue
                    res += 1
                    grid[newR][newC] = 0
                    q.append((newR, newC))
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        
        return area

        
