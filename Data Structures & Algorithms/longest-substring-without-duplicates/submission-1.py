class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        maxLength = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            length = R - L + 1
            maxLength = max(maxLength, length)
            seen.add(s[R])
        return maxLength
                