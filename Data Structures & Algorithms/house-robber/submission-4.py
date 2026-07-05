class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        copy = nums.copy()
        copy[1] = max(copy[0], copy[1])

        for i in range(2, len(copy)):
            copy[i] = max(copy[i - 1], copy[i - 2] + copy[i])
        return max(copy)