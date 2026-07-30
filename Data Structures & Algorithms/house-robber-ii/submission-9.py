class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(nums):
            prev1, prev2 = 0, 0

            for num in nums:
                current = max(prev1 + num, prev2)
                prev1 = prev2
                prev2 = current
            return prev2
        if len(nums) == 1: return nums[0]
        return max(robber(nums[1:]), robber(nums[:-1]))
