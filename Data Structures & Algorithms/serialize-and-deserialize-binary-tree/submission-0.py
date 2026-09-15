# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N#"

        s = str(root.val) + "#"
        s += self.serialize(root.left)
        s += self.serialize(root.right)

        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        def recur(s):
            i = 0
            while s[i] != "#":
                i += 1

            val = s[:i]
            s = s[i+1:]

            if val == "N":
                return [None, s]
            
            left = recur(s)
            s = left[1]
            right = recur(s)
            s = right[1]

            return [TreeNode(int(val), left[0], right[0]), s]

        return recur(data)[0]
