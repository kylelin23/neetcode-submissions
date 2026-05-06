class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        boxes = {}

        for i in range(9): 
            for j in range(9): 
                if board[i][j] == '.': 
                    continue
                
                if i not in rows: 
                    rows[i] = []
                rows[i].append(board[i][j])

                if j not in columns: 
                    columns[j] = []
                columns[j].append(board[i][j])

                temp = []
                temp.append(i//3)
                temp.append(j//3)
                temp = tuple(temp)
                if temp not in boxes: 
                    boxes[temp] = []
                boxes[temp].append(board[i][j])
                
               
                
                
        for row in rows.values(): 
            if len(row) != len(set(row)): 
                return False
        
        for column in columns.values(): 
            if len(column) != len(set(column)): 
                return False

        for box in boxes.values(): 
            if len(box) != len(set(box)): 
                return False
        return True