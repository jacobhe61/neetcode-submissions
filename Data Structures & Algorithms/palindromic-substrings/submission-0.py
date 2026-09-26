class Solution:
    def helper(self, L, R, s):
        count = 0
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
            count += 1
        
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            L = i
            R = i

            count += self.helper(L, R, s)

            L = i
            R = i+1

            count += self.helper(L, R, s)

        return count