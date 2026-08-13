class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def bfs(x, y):
            if (x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1"):
                return
               
            grid[x][y] = "#"
            diff = (
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            )
            
            for dx, dy in diff:                
                bfs(x + dx, y + dy)
                                                    
        # loop the array
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "#":
                    continue
                elif grid[i][j] == "0":
                    grid[i][j] = "#"
                elif grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        
        return res