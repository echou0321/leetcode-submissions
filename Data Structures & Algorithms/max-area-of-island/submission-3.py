class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0
        
        def bfs(r, c):
            q = collections.deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row + dr, col + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        grid[newR][newC] = 0
                        q.append((newR, newC))
                        area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea