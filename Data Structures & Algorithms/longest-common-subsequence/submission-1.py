class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if len(text2) > len(text1):
            w = len(text1)
            l = len(text2)
            s1 = text2
            s2 = text1
        else:
            w = len(text2)
            l = len(text1)
            s1 = text1
            s2 = text2

        prev = [0] * (w+1)

        for i in range(l-1, -1, -1):
            curr = [0] * (w+1)
            for j in range(w-1, -1, -1):
                if s1[i] == s2[j]:
                    curr[j] = prev[j+1] + 1
                else:
                    curr[j] = max(prev[j], curr[j+1])
            prev = curr

        return prev[0]