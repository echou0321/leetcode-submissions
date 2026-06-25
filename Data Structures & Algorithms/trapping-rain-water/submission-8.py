class Solution:
    def trap(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        lmax, rmax = heights[l], heights[r]

        while l < r:
            if heights[l] < heights[r]:
                l += 1
                lmax = max(lmax, heights[l])
                res += lmax - heights[l]
            else:
                r -= 1
                rmax = max(rmax, heights[r])
                res += rmax - heights[r] 
        return res