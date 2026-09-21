# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {inorder[i]: i for i in range(len(inorder))}
        p = 0

        def dfs(i_l, i_r):
            if i_l > i_r:
                return None
    
            nonlocal p
            root = TreeNode(preorder[p])
            p += 1
    
            split = cache[root.val]
            root.left = dfs(i_l, split - 1)
            root.right = dfs(split + 1, i_r)
    
            return root
        
        return dfs(0, len(inorder) - 1)