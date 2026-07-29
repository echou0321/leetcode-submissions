class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = {}
        l = 0
        r = 0
        while r < len(s2):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if (r - l + 1) > len(s1):
                count2[s2[l]] = count2.get(s2[l], 0) - 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            if count1 == count2:
                return True
            r += 1
        return False
