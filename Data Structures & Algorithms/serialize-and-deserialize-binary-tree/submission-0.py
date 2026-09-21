# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def dfs(node):
            nonlocal vals
            if not node:
                vals.append("$")
                return
            
            vals.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "#".join(vals)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split("#")
        i = 0

        def dfs():
            nonlocal i
            nonlocal vals

            if i >= len(vals):
                return
            
            val = vals[i]
            i += 1
            if val == "$":
                return None
            
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()