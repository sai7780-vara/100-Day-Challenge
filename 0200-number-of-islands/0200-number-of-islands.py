class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            # Boundary and visited check
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            # Mark current cell as visited
            grid[i][j] = '0'
            # Explore all 4 directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count
