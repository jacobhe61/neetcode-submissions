class MedianFinder:

    def __init__(self):
        self.length = 0
        self.top = []
        self.bottom = []

    def addNum(self, num: int) -> None:
        if self.length % 2:
            if num > self.top[0]:
                heapq.heappush_max(self.bottom, heapq.heappushpop(self.top, num))
            else:
                heapq.heappush_max(self.bottom, num)
        else:
            if not self.top or num > self.top[0]:
                heapq.heappush(self.top, num)
            else:
                heapq.heappush(self.top, heapq.heappushpop_max(self.bottom, num))
        self.length += 1

    def findMedian(self) -> float:
        if not self.bottom or self.length % 2:
            return self.top[0]
        return (self.top[0] + self.bottom[0])/2
        