class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        def traverse(r, c):
            nonlocal fresh
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                traverse(r + 1, c)
                traverse(r - 1, c)
                traverse(r, c + 1)
                traverse(r, c - 1)
            time += 1
        
        return time if fresh == 0 else -1
