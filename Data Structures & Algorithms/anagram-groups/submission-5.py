class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord("a")] += 1
            index = tuple(count)
            grouped[index] = grouped.get(index, [])
            grouped[index].append(s)
        lists = []
        for k in grouped:
            lists.append(grouped[k])
        return lists