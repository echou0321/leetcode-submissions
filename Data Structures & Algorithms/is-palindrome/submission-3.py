class Solution:
    def isPalindrome(self, s: str) -> bool:
        #solution one. more memory use
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        
        #solution 2 (with pointers). this is recommended solution 
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
        return True

            

        