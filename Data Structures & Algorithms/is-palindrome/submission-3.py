class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        while not s[L].isalnum():
            L += 1
            if L > R:
                return True
        while not s[R].isalnum():
            R -= 1
        while L < R:
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
            while not s[L].isalnum():
                L += 1
            while not s[R].isalnum():
                R -= 1
        return True