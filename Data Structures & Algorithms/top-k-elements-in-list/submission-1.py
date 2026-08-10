class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        frequencies = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            frequencies[freq].append(num)
        
        result = []
        for i in reversed(frequencies):
            for j in i:
                if len(result) != k:
                    result.append(j)
        
        return result