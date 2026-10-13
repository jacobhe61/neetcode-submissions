"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s = 0
        e = 0

        res = 0
        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                s += 1
            else:
                e += 1
            res = max(res, s-e)

        return res
