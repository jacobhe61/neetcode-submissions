class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = [0] * 26
        for c in s1:
            s1Counts[ord(c) - ord("a")] += 1

        s2Counts = [0] * 26
        L = 0
        for R in range(len(s2)):
            s2Counts[ord(s2[R]) - ord("a")] += 1
            if R - L + 1 > len(s1):
                s2Counts[ord(s2[L]) - ord("a")] -= 1
                L += 1
            if s1Counts == s2Counts:
                return True
        return False