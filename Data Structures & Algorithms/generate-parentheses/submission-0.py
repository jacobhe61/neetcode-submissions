class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recur(s, open, closed):
            if not open and not closed:
                res.append(s)
                return

            elif not open:
                recur(s + ")", open, closed - 1)
            
            elif open == closed:
                recur(s + "(", open - 1, closed)

            else:
                recur(s + "(", open - 1, closed)
                recur(s + ")", open, closed - 1)
            return
        
        recur("", n, n)
        return res