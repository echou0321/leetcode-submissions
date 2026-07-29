class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l, r = 0, 0
        maxFreq = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(count.values())

            if (r - l + 1) - maxFreq <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            r += 1
        return res
            