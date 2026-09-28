class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        
        def dfs(node):
            seen.add(node)
            for neighbour in graph[node]:
                if neighbour not in seen:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in seen:
                components += 1
                dfs(i)

        return components