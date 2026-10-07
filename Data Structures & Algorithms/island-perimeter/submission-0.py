class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0

            visit.add((i,j))
            perim = dfs(i + 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i - 1, j)
            return perim

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i,j)
        return 0