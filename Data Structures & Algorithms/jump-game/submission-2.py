class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(0, n - 1):
            if nums[i] == 0:
                clearable = False
                for j in range(i - 1, -1, -1):
                    if j + nums[j] > i:
                        clearable = True
                        break
                if not clearable:
                    return False
        return True