class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s2) > len(s1):
            w = len(s1)
            l = len(s2)
            wStr = s1
            lStr = s2
        else:
            w = len(s2)
            l = len(s1)
            wStr = s2
            lStr = s1
        
        prev = [False] * (w+1)

        if l + w != len(s3):
            return False

        for i in range(l, -1, -1):
            curr = [False] * (w+1)
            for j in range(w, -1, -1):
                if i == l and j == w:
                    curr[j] = True
                elif j < w and wStr[j] == s3[i+j] and curr[j+1]:
                    curr[j] = True
                elif i < l and lStr[i] == s3[i+j] and prev[j]:
                    curr[j] = True
            prev = curr
        
        return prev[0]