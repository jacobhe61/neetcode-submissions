class Solution:
    def isPalindrome(self, s):
        L = 0
        R = len(s)-1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def recur(i, arr):
            if i >= len(s):
                if self.isPalindrome(arr[-1]):
                    res.append(arr.copy())
                return

            if not arr or self.isPalindrome(arr[-1]):
                arr.append(s[i])
                recur(i+1, arr)
                arr.pop()
            
            if arr:
                arr[-1] += s[i]
                recur(i+1, arr)

            return
        
        recur(0, [])
        return res