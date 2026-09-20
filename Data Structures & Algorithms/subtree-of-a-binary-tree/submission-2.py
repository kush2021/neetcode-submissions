# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(a, b):
            if not a and not b:
                return True
            if a and b:
                return a.val == b.val and equal(a.left, b.left) and equal(a.right, b.right)
            return False

        if not root and not subRoot:
            return True

        match = None
        if root and subRoot:
            if root.val == subRoot.val:
                match = equal(root, subRoot)
            return match or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return False