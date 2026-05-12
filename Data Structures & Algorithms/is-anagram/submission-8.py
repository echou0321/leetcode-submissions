class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countT, countS = {}, {}

        for i in range(len(s)):
            countT[t[i]] = countT.get(t[i], 0) + 1
            countS[s[i]] = countS.get(s[i], 0) + 1
        for c in countT:
            if countT[c] != countS.get(c):
                return False
        
        return True
