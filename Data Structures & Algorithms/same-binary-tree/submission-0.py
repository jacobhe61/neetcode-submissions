# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, curr1, curr2):
        if curr1 and not curr2:
            return False
        if curr2 and not curr1:
            return False
        if not curr1 and not curr2:
            return True
        return curr1.val == curr2.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        curr1 = p
        curr2 = q
        stack1 = []
        stack2 = []

        while curr1 or stack1 or curr2 or stack2:
            if not self.isEqual(curr1, curr2):
                return False
            if curr1 and curr2:
                stack1.append(curr1)
                stack2.append(curr2)
                curr1 = curr1.left
                curr2 = curr2.left
            else:
                curr1 = stack1.pop()
                curr2 = stack2.pop()
                if not self.isEqual(curr1, curr2):
                    return False
                curr1 = curr1.right
                curr2 = curr2.right
        return True
                
                
