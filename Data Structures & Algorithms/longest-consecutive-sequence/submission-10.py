class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                curr = 0
                while (num + curr) in numSet:
                    curr += 1
                    res = max(res, curr)

        return res