class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row        
        for i in range(len(board)):
            row_set = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row_set:
                    return False
                else:
                    row_set.add(board[i][j])

        # check column        
        for x in range(len(board[0])):
            column_set = set()
            for y in range(len(board)):
                if board[y][x] == ".":
                    continue
                elif board[y][x] in column_set:
                    return False
                else:
                    column_set.add(board[y][x])

        top_left = [
            (0,0),
            (3,0),
            (6,0),
            (0,3),
            (3,3),
            (6,3),
            (0,6),
            (3,6),
            (6,6),
        ]

        for a, b in top_left:
            square_set = set()
            for da in range(0,3):
                for db in range(0,3):
                    if board[a + da][b + db] == ".":
                        continue
                    elif board[a + da][b + db] in square_set:
                        return False
                    else:
                        square_set.add(board[a+da][b+db])
        
        return True




        