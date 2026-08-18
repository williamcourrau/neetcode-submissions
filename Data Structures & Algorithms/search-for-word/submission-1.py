class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r, c, combination):
            if r < 0 or c < 0 or c >= COLS or r >= ROWS:
                return False
            
            if board[r][c] != word[len(combination)]: 
                return False
            
            
            current_word = board[r][c]
            combination += current_word
            if combination == word:
                return True

            board[r][c] = "#"

            result = (dfs(r + 1, c, combination) or
                      dfs(r - 1, c, combination) or
                      dfs(r, c + 1, combination) or
                      dfs(r, c - 1, combination))
            
            board[r][c] = current_word
            
            return result
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in word:
                    if dfs(r, c, ""):
                        return True
        
        return False
