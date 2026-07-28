class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = Counter(s)
        countT = Counter(t)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True