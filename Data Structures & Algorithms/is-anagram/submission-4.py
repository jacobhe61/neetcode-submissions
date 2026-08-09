class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        countt = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counts[s[i]] += 1
            countt[t[i]] += 1
        return counts == countt