class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            q = collections.deque()
            grid[r][c] = 0
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row + dr, col + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == "1":
                        grid[newR][newC] = 0
                        q.append((newR, newC))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands
