class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    newR, newC = dr + r, dc + c
                    if (0 <= newR < rows and 
                        0 <= newC < cols and
                        grid[newR][newC] == 1):

                        grid[newR][newC] = 2
                        fresh -= 1
                        q.append((newR, newC))
            minutes += 1

        return minutes if fresh == 0 else -1        
