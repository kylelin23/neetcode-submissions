class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        three_by_threes = {}
        for i in range(len(board)): 
            for j in range(len(board[i])):
                if board[i][j] != '.': 
                    if i in rows: 
                        rows[i].append(board[i][j])
                    else: 
                        rows[i] = []
                        rows[i].append(board[i][j])

                    if j in columns: 
                        columns[j].append(board[i][j])
                    else: 
                        columns[j] = []
                        columns[j].append(board[i][j])

                    three_by_three = []
                    three_by_three.append(i // 3)
                    three_by_three.append(j // 3)
                    three_by_three = tuple(three_by_three)
                    if three_by_three in three_by_threes: 
                        three_by_threes[three_by_three].append(board[i][j])
                    else: 
                        three_by_threes[three_by_three] = []
                        three_by_threes[three_by_three].append(board[i][j])
        for row in rows: 
            if len(rows[row]) != len(set(rows[row])): 
                return False
        
        for column in columns: 
            if len(columns[column]) != len(set(columns[column])): 
                return False
        
        for three_by_three in three_by_threes: 
            if len(three_by_threes[three_by_three]) != len(set(three_by_threes[three_by_three])): 
                return False
        
        return True