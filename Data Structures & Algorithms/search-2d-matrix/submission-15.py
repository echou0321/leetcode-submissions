class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        top, bot = 0, rows - 1

        while top <= bot:
            mRow = (top + bot) // 2
            if target < grid[mRow][0]:
                bot = mRow - 1
            elif target > grid[mRow][-1]:
                top = mRow + 1
            else:
                l, r = 0, cols - 1

                while l <= r:
                    m = (l + r) // 2
                    if target < grid[mRow][m]:
                        r = m - 1
                    elif target > grid[mRow][m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False