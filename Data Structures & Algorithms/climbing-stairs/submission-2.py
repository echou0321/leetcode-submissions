class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            current = one + two
            two = one
            one = current
        
        return one