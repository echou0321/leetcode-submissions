class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            mRow = (top + bot) // 2
            if target < matrix[mRow][0]:
                bot = mRow - 1
            elif target > matrix[mRow][-1]:
                top = mRow + 1
            else:
                l, r = 0, cols - 1
                while l <= r:
                    m = (l + r) // 2
                    if target < matrix[mRow][m]:
                        r = m - 1
                    elif target > matrix[mRow][m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False