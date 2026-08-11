class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chaintop = {}
        chainbot = {}
        for i in nums:
            if i not in chaintop and i not in chainbot:
                if i-1 in chaintop and i+1 in chainbot:
                    newlen = chaintop[i-1] + chainbot[i+1] + 1
                    chaintop[i+chainbot[i+1]] = newlen
                    chainbot[i-chaintop[i-1]] = newlen
                    chaintop.pop(i-1)
                    chainbot.pop(i+1)
                elif i-1 in chaintop:
                    newlen = chaintop[i-1] + 1
                    chaintop[i] = newlen
                    chainbot[i-chaintop[i-1]] = newlen
                    chaintop.pop(i-1)
                elif i+1 in chainbot:
                    newlen = chainbot[i+1] + 1
                    chainbot[i] = newlen
                    chaintop[i+chainbot[i+1]] = newlen
                    chainbot.pop(i+1)
                else:
                    chaintop[i] = 1
                    chainbot[i] = 1
        high = 0
        for key, value in chaintop.items():
            if value > high:
                high = value
        return high