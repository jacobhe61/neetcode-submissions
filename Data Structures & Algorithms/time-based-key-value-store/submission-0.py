class TimeMap:

    def __init__(self):
        self.tMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tMap[key].append(tuple([value, timestamp]))

    def get(self, key: str, timestamp: int) -> str:
        L = 0
        R = len(self.tMap[key]) - 1
        val = ""

        while L <= R:
            M = (L+R)//2

            if self.tMap[key][M][1] < timestamp:
                L = M + 1
                val = self.tMap[key][M][0]

            elif self.tMap[key][M][1] > timestamp:
                R = M - 1
            else:
                return self.tMap[key][M][0]
        return val