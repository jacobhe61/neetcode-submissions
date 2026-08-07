class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord("a")] += 1
            grouped[tuple(count)].append(s)
        return list(grouped.values())