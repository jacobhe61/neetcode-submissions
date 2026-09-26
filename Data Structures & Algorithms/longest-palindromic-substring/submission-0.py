class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0

        for i in range(len(s)):
            L = i
            R = i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L+1 > length:
                    length = R-L+1
                    resL = L
                    resR = R
                L -= 1
                R += 1

            L = i
            R = i+1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L+1 > length:
                    length = R-L+1
                    resL = L
                    resR = R
                L -= 1
                R += 1
        
        return s[resL:resR+1]