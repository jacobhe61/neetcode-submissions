# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def recur(root):
            if not root or (not root.right and not root.left):
                return tuple([1, 1])

            right = recur(root.right)
            left = recur(root.left)

            if not root.left:
                curr = right[0] + 1
                high = right[1]
                high = max(curr, high)
                return tuple([curr, high])
            if not root.right:
                curr = left[0] + 1
                high = left[1]
                high = max(curr, high)
                return tuple([curr, high])
            tree = 1 + right[0] + left[0]
            curr = 1 + max(right[0], left[0])
            high = max(curr, tree, right[1], left[1])
            return tuple([curr, high])
        
        pair = recur(root)
        return pair[1] - 1