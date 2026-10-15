class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        sol = [0] * (len(num1) + len(num2))
        res = [""] * (len(num1) + len(num2))
        
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                product = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p = product % 10
                c = product // 10

                sol[i + j + 1] += p
                sol[i + j] += c

        carry = 0
        for i in range(len(sol)-1, -1, -1):
            sol[i] += carry
            carry = sol[i] // 10
            sol[i] %= 10

        while len(sol) > 1 and not sol[0]:
            sol.pop(0)
        
        for i in range(len(sol)):
            res[i] = str(sol[i])

        return "".join(res)