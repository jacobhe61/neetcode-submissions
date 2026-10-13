class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedInts = sorted(intervals, key=lambda x: (x[0], x[1]))

        res = []
        temp = sortedInts[0]
        for i in range(1, len(sortedInts)):
            if temp[1] >= sortedInts[i][0]:
                temp = [min(temp[0], sortedInts[i][0]), max(temp[1], sortedInts[i][1])]
            else:
                res.append(temp)
                temp = sortedInts[i]
        
        return res + [temp]