class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point

        res = 0
        for (x, y), hCorner in self.points.items():
            yLen = py - y
            xLen = px - x

            if abs(yLen) != abs(xLen) or xLen == yLen == 0:
                continue

            yCorner = self.points[(px - xLen, py)] if (px - xLen, py) in self.points else 0
            xCorner = self.points[(px, py - yLen)] if (px, py - yLen) in self.points else 0

            res += hCorner * yCorner * xCorner
        
        return res
        
