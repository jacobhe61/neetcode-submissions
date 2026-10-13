class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        res = []
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if temp[1] >= intervals[i][0]:
                temp = [min(temp[0], intervals[i][0]), max(temp[1], intervals[i][1])]
            else:
                res.append(temp)
                temp = intervals[i]
        
        return res + [temp]