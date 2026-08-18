class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        directions = (
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        )
    
        def dfs(x, y):            
            grid[x][y] = "0"
            for dx, dy in directions:
                if 0 <= (x + dx) < row and 0 <= (y + dy) < col and grid[x + dx][y+dy] == "1":
                    dfs(x + dx, y + dy)                                    
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    continue
                elif grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res

                


        