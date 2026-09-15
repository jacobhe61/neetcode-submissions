class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height)-1
        level = 0
        water = 0
        last = 0
        while L < R:
            newLevel = min(height[L], height[R])
            if last == 1:
                water -= min(level, height[L])
            elif last == 2:
                water -= min(level, height[R])
            if newLevel > level:
                water += (newLevel - level) * (R - L - 1)
                level = newLevel
            if height[L] > height[R]:
                R -= 1
                last = 2
            else:
                L += 1
                last = 1
        return water