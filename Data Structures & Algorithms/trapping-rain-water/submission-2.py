class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            level = 0
            while len(stack) != 0 and stack[-1][1] <= height[i]:
                elem = stack.pop()
                newLevel = elem[1]
                water += (newLevel - level) * (i - elem[0] - 1)
                level = newLevel
            if len(stack) != 0:
                water += (height[i] - level) * (i - stack[-1][0] - 1)
            stack.append([i, height[i]])
        return water