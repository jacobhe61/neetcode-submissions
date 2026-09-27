class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        seen = {0}

        if sum(nums) % 2:
            return False

        half = sum(nums) / 2
        
        for n in nums:
            if half - n in seen:
                return True
            
            for m in seen.copy():
                if n+m not in seen and n+m < half:
                    seen.add(n+m)

        return False