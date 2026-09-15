# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        i = 0
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                i += 1
                curr = stack.pop()
                if i >= k:
                    return curr.val
                curr = curr.right
        return 0