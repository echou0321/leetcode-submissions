class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1,0]]
        cols, rows = len(grid[0]), len(grid)

        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row + dr, col + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == "1":
                        grid[newR][newC] = "0"
                        q.append((newR, newC))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands
