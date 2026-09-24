class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            bfs(i - 1, j)
            bfs(i + 1, j)
            bfs(i, j - 1)
            bfs(i, j + 1)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1":
                    islands += 1
                    bfs(i, j)

        return islands