class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        rain = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                lMax = max(height[l], lMax)
                rain += lMax - height[l]
            else:
                r -= 1
                rMax = max(height[r], rMax)
                rain += rMax - height[r]
        
        return rain
            