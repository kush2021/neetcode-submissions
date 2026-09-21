# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root):
            vals = []

            if root.left:
                vals.extend(traverse(root.left))
            vals.append(root.val)
            if root.right:
                vals.extend(traverse(root.right))

            return vals
            
        return traverse(root)[k - 1]