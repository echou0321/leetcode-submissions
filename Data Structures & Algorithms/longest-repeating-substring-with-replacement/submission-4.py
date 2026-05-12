class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            window  = r - l + 1
            maxFreq = max(maxFreq, count.get(s[r]))
            if window - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res