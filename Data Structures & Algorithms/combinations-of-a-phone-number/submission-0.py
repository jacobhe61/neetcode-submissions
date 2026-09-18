class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        charMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        
        def recur(i, stack):
            if i >= len(digits):
                res.append("".join(stack))
                return

            s = charMap[digits[i]]
            for c in s:
                stack.append(c)
                recur(i+1, stack)
                stack.pop()
            
            return

        recur(0, [])
        return res