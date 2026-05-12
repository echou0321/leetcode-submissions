class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR = dr + row
                    newC = dc + col
                    if (newR < 0 or newC < 0 or newR >= rows or
                        newC >= cols or grid[newR][newC] == "0"):
                        continue
                    grid[newR][newC] = "0"
                    q.append((newR, newC))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands








