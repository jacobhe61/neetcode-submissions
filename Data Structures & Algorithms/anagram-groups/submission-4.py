class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs:
            index = [0] * 26
            for i in range(len(s)):
                index[ord(s[i]) - ord("a")] += 1
            grouped[tuple(index)] = grouped.get(tuple(index), [])
            grouped[tuple(index)].append(s)
        lists = []
        for k in grouped:
            lists.append(grouped[k])
        return lists