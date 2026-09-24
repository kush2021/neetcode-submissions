"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cache = {}
        q = deque()
        q.append(node)
        seen = {node.val}
        while len(q) != 0:
            cur = q.popleft()
            new = Node()
            new.val = cur.val
            cache[new.val] = new
            for n in cur.neighbors:
                if n.val not in seen:
                    q.append(n)
                    seen.add(n.val)
        
        q.append(node)
        seen = {node.val}
        while len(q) != 0:
            cur = q.popleft()
            new = cache[cur.val]
            ns = []
            for n in cur.neighbors:
                ns.append(cache[n.val])
                if n.val not in seen:
                    q.append(n)
                    seen.add(n.val)
            new.neighbors = ns

        return cache[node.val]