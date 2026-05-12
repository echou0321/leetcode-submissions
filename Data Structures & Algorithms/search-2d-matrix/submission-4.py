class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l, r = 0, len(row) - 1
            if row[l] <= target <= row[r]:
                while l <= r:
                    m = (l + r) //2
                    if target < row[m]:
                        r = m - 1
                    elif target > row[m]:
                        l = m + 1
                    else:
                        return True
        return False
                        