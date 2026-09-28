class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(p1, p2):
            if p1 >= len(word1) and p2 >= len(word2):
                return 0
            
            elif p1 >= len(word1):
                return len(word2) - p2
            
            elif p2 >= len(word2):
                return len(word1) - p1

            if tuple([p1, p2]) in dp:
                return dp[tuple([p1, p2])]
            
            if word1[p1] == word2[p2]:
                dp[tuple([p1, p2])] = dfs(p1+1, p2+1)
            else:
                dp[tuple([p1, p2])] = 1 + min(dfs(p1+1, p2), dfs(p1, p2+1), dfs(p1+1, p2+1))

            return dp[tuple([p1, p2])]

        return dfs(0, 0)