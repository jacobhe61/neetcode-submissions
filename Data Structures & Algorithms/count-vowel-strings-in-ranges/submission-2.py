class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        sums = [0] * len(words)

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                sums[i] += 1
            if i > 0:
                sums[i] += sums[i-1]

        res = []    
        for li, ri in queries:
            rightNum = sums[ri]
            leftNum = sums[li-1] if li else 0
            res.append(rightNum - leftNum)
        
        return res
