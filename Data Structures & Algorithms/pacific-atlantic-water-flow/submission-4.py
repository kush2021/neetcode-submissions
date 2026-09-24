class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        results = []

        def dfs_p(i, j):
            height = heights[i][j]
            pacific.add((i, j))
            
            if (i + 1, j) not in pacific and i + 1 < m and height <= heights[i + 1][j]:
                dfs_p(i + 1, j)
            if (i, j + 1) not in pacific and j + 1 < n and height <= heights[i][j + 1]:
                dfs_p(i, j + 1)
            if (i - 1, j) not in pacific and i - 1 >= 0 and height <= heights[i - 1][j]:
                dfs_p(i - 1, j)
            if (i, j - 1) not in pacific and j - 1 >= 0 and height <= heights[i][j - 1]:
                dfs_p(i, j - 1)
        
        def dfs_a(i, j):
            height = heights[i][j]
            atlantic.add((i, j))
            
            if (i - 1, j) not in atlantic and i - 1 >= 0 and height <= heights[i - 1][j]:
                dfs_a(i - 1, j)
            if (i, j - 1) not in atlantic and j - 1 >= 0 and height <= heights[i][j - 1]:
                dfs_a(i, j - 1)
            if (i + 1, j) not in atlantic and i + 1 < m and height <= heights[i + 1][j]:
                dfs_a(i + 1, j)
            if (i, j + 1) not in atlantic and j + 1 < n and height <= heights[i][j + 1]:
                dfs_a(i, j + 1)

        pacific = set()
        atlantic = set()
        for i in range(m):
            dfs_p(i, 0)
            dfs_a(i, n - 1)
        for i in range(n):
            dfs_p(0, i)
            dfs_a(m - 1, i)

        both = pacific & atlantic
        return list(both)