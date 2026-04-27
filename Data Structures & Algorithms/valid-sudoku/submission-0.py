class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows: 
        rows = {}
        columns = {}
        three_by_three = {}
        for i in range(len(board)): 
            for j in range(len(board[i])): 
            
                if board[i][j] != '.': 
                    if int(board[i][j]) < 1 or int(board[i][j]) > 9: 
                        return False
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
 
                    coords = []
                    coords.append(i//3)
                    coords.append(j//3)
                    coords = tuple(coords)
                    if coords in three_by_three: 
                        three_by_three[coords].append(board[i][j])
                    else: 
                        three_by_three[coords] = []
                        three_by_three[coords].append(board[i][j])
        print(rows)
        print(columns)
        print(three_by_three)
        for row in rows.values(): 
            if len(row) != len(set(row)): 
                return False
        
        for column in columns.values(): 
            if len(column) != len(set(column)): 
                return False

        for box in three_by_three.values(): 
            if len(box) != len(set(box)): 
                return False
        
        return True