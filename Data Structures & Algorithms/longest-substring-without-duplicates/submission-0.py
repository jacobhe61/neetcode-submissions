class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        L = 0
        maxLength = 1
        seen.add(s[0])
        for R in range(1, len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            length = R - L + 1
            if length > maxLength:
                maxLength = length
            seen.add(s[R])
        return maxLength
                