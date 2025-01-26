class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)


        #capture unsurrounded regions and turn them to temp variable (O -> T)
        for c in range(COLS):
            capture(0, c)
            capture(ROWS-1, c)
        
        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS-1)
        
        #capture surrounded regions O -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

                #uncaptured regions (T -> O)
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        