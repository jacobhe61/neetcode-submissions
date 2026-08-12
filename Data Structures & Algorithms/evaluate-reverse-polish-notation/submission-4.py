class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i == "+":
                nums[len(nums)-2] = nums[len(nums)-2] + nums[len(nums)-1]
                nums.pop()
            elif i == "-":
                nums[len(nums)-2] = nums[len(nums)-2] - nums[len(nums)-1]
                nums.pop()
            elif i == "*":
                nums[len(nums)-2] = nums[len(nums)-2] * nums[len(nums)-1]
                nums.pop()
            elif i == "/":
                nums[len(nums)-2] = int(nums[len(nums)-2] / nums[len(nums)-1])
                nums.pop()
            else:
                nums.append(int(i))
        return nums[0]