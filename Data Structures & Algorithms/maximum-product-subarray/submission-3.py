class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
                continue
            temp = currMax * num
            currMax = max(temp, currMin * num, num)
            currMin = min(temp, currMin * num, num)
            res = max(res, currMax)
        
        return res