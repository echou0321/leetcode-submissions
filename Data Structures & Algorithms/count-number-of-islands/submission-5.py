class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nR, nC = row + dr, col + dc
                    if 0 <= nR < rows and 0 <= nC < cols and grid[nR][nC] == "1":
                        grid[nR][nC] = "0"
                        q.append((nR, nC))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands





