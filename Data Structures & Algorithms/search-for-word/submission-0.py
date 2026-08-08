class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtracking(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS):
                return False
            
            if word[index] != board[row][col] or board[row][col] == "#":
                return False
            
            board[row][col] = "#"
            res = (backtracking(row + 1, col, index + 1) or
                   backtracking(row - 1, col, index + 1) or
                   backtracking(row, col + 1, index + 1) or
                   backtracking(row, col -1, index + 1))
            board[row][col] = word[index]
            return res
        
        for i in range(ROWS):
            for x in range(COLS):
                if backtracking(i, x, 0):
                    return True
        
        return False