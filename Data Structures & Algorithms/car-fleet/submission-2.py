class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = reversed(sorted(range(len(position)), key=lambda k: position[k]))
        fleetCount = 1
        limit = -1
        for i in indices:
            if limit != -1:
                curdistance = target - position[i]
                limitdistance = target - position[limit]
                curtime = curdistance / speed[i]
                limittime = limitdistance / speed[limit]
                if curtime > limittime:
                    fleetCount += 1
                    limit = i
            else:
                limit = i
        return fleetCount
        