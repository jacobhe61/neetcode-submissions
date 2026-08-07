class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs:
            index = "".join(sorted(s))
            grouped[index] = grouped.get(index, [])
            grouped[index].append(s)
        lists = []
        for k in grouped:
            lists.append(grouped[k])
        return lists