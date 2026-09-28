class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            l = min(len(a), len(b))
            if len(a) > len(b) and a[:l] == b[:l]:
                return ""
            for j in range(l):
                if a[j] != b[j]:
                    graph[a[j]].add(b[j])
                    break

        seen = {}
        order = []
        
        def dfs(node):
            if node in seen:
                return seen[node]
            seen[node] = True

            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True

            seen[node] = False
            order.append(node)

        for c in graph:
            if dfs(c):
                return ""
        
        order.reverse()
        return "".join(order)