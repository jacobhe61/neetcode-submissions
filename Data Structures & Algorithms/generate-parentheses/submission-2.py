class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def recur(open, closed):
            if not open and not closed:
                res.append("".join(s))
                return

            elif not open:
                s.append(")")
                recur(open, closed - 1)
                s.pop()
            
            elif open == closed:
                s.append("(")
                recur(open - 1, closed)
                s.pop()

            else:
                s.append("(")
                recur(open - 1, closed)
                s.pop()
                s.append(")")
                recur(open, closed - 1)
                s.pop()
            return
        
        recur(n, n)
        return res