class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, res = 0, nums[0]

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            res = max(currSum, res)

        return res