class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {}
        cols = {}
        three_by_three = {}

        for i in range(len(board)): 
            for j in range(len(board[i])): 
                print(rows)
                print(cols)
                print(three_by_three)
                val = board[i][j]
                if val == '.': 
                    continue
                key = []
                key.append(i//3)
                key.append(j//3)
                key = tuple(key)

                if i not in rows: 
                    rows[i] = []
                rows[i].append(val)

                if j not in cols: 
                    cols[j] = []
                cols[j].append(val)

                
                if key not in three_by_three: 
                    three_by_three[key] = []
                three_by_three[key].append(val)

        for row in rows.values():
            if len(row) != len(set(row)): 
                return False 

        for col in cols.values():
            if len(col) != len(set(col)): 
                return False 

        for i in three_by_three.values():
            if len(i) != len(set(i)): 
                return False 

        return True