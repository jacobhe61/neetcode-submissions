import math

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) > len(word1):
            w = len(word1)
            l = len(word2)
            wStr = word1
            lStr = word2
        else:
            w = len(word2)
            l = len(word1)
            wStr = word2
            lStr = word1

        prevDp = [math.inf] * (w+1)

        for i in range(l, -1, -1):
            currDp = [l-i] * (w+1)
            for j in range(w-1, -1, -1):
                if i < l and lStr[i] == wStr[j]:
                    currDp[j] = prevDp[j+1]
                else:
                    currDp[j] = 1 + min(currDp[j+1], prevDp[j], prevDp[j+1])
            prevDp = currDp

        return prevDp[0]