class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(x, y):            
            if (
                x < 0 or x >= rows or
                y < 0 or y >= cols or
                grid[x][y] != "1"
            ):
                return
            
            grid[x][y] = "#"

            directions = (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            )

            for dx, dy in directions:
                dfs(x + dx, y + dy)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res