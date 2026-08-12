class Solution:
    def isValid(self, s: str) -> bool:
        paren = ["0"]
        for c in s:
            if c == "(":
                paren.append("(")
            elif c == "{":
                paren.append("{")
            elif c == "[":
                paren.append("[")
            elif c == ")":
                if paren.pop() != "(":
                    return False
            elif c == "]":
                if paren.pop() != "[":
                    return False
            elif c == "}":
                if paren.pop() != "{":
                    return False
        if len(paren) != 1:
            return False
        return True