class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            for c in s:
                code += c
                code += c
            code += "()"
        return code

    def decode(self, s: str) -> List[str]:
        strs = [""]
        strnum = 0
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                strs[strnum] += s[i]
            else:
                strs.append("")
                strnum += 1
        strs.pop()
        return strs
            