class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0, 1]

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                temp = dp[1]
                dp[1] = 0
                dp[0] = temp
                continue

            count = 0
            count += dp[1]
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                count += dp[0]

            temp = dp[1]
            dp[1] = count
            dp[0] = temp
        
        return dp[1]