class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
                continue
            temp1 = currMax * num
            temp2 = currMin * num 
            currMax = max(temp1, temp2, num)
            currMin = min(temp1, temp2, num)
            res = max(currMax, res)
        return res 