class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        count = 0
        for c in t:
            tCount[c] += 1
            if tCount[c] == 1:
                count += 1
        
        sCount = defaultdict(int)
        match = 0
        length = len(s) + 1
        result = ""
        L = 0
        for R in range(len(s)):
            sCount[s[R]] += 1
            if sCount[s[R]] == tCount[s[R]]:
                match += 1
            while match == count:
                if R - L + 1 < length:
                    length = R - L + 1
                    result = s[L:R+1]
                sCount[s[L]] -= 1
                if sCount[s[L]] == tCount[s[L]] - 1:
                    match -= 1
                L += 1
        return result
        
