class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()

        def dfs(i):
            seen.add(i)
            for j in graph[i]:
                if j not in seen:
                    dfs(j)
        
        dfs(0)

        return len(seen) == n