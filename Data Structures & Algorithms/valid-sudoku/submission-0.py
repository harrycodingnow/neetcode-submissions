class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        col = set()
        
        # check row
        for n in range(0,9):
            row = set()
            for m in range(0,9):
                if board[n][m] == ".":
                    continue
                elif board[n][m] in row:
                    return False
                else:
                    row.add(board[n][m])

        # check column
        for x in range(0, 9):
            col = set()            
            for y in range(0, 9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in col: 
                    return False
                else:
                    col.add(board[y][x])

        # check sub-boxes
        starting_point = [
            (0,0),
            (0,3),
            (0,6),
            (3,0),
            (3,3),
            (3,6),
            (6,0),
            (6,3),
            (6,6),            
            ]
        for x, y in starting_point:
            square = set()
            for dx in range(0, 3):
                for dy in range(0, 3):
                    if board[x+dx][y+dy] == ".":
                        continue
                    elif board[x+dx][y+dy] in square:
                        return False
                    else:
                        square.add(board[x+dx][y+dy])
        return True

        





        
        