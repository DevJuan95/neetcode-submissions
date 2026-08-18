class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create a counter for row, columns and boxes

        for i in range(9):
            row_counter = []
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in row_counter:
                        return False
                    row_counter.append(board[i][j])

        for i in range(9):
            column_counter = []
            for j in range(9):
                if board[j][i].isnumeric():
                    if board[j][i] in column_counter:
                        return False
                    column_counter.append(board[j][i])

        for r in range(0, 9, 3):
            for c in range(0 , 9, 3):
                sub_matrix_counter = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if not board[i][j].isnumeric():
                            continue
                        if board[i][j] in sub_matrix_counter:
                            return False
                        sub_matrix_counter.append(board[i][j])
        
        return True
