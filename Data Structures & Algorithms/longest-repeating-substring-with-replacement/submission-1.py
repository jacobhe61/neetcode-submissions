class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        counts = [0] * 26
        high = 0
        result = 0
        for R in range(len(s)):
            counts[ord(s[R]) - ord("A")] += 1
            high = max(counts[ord(s[R]) - ord("A")], high)
            while high + k < R - L + 1:
                counts[ord(s[L]) - ord("A")] -= 1
                L += 1
            result = max(R - L + 1, result)
        return result