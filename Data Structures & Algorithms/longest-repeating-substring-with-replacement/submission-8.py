class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        # To keep track of count of most common letter
        maxFreq = 0
        for r in range(len(s)):
            # This updates the count of a given letter as the window expands
            count[s[r]] = 1 + count.get(s[r], 0)
            # This keeps track of the count of the most common letter in window
            maxFreq = max(maxFreq, count.get(s[r]))

            # This makes sure that our window - maxFreq stays within k
            # so that we keep track the relevant window length.
            # When we exceed the relevant range (where it takes more than k swaps),
            # we increment the left pointer and decrease the count of the letter
            # at the left pointer
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            # res keeps track of the max valid range
            res = max(res, r - l + 1)

        return res
            
