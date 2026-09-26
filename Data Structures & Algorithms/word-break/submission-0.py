class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * len(s)

        for i in range(len(s)-1, -1, -1):
            for j in wordDict:
                if (s[i:i+len(j)] == j) and (i+len(j) == len(s) or dp[i+len(j)] == True):
                    dp[i] = True
        
        return dp[0]
                    

        