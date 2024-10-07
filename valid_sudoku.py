class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #helper function to check for duplicates in list
        def dupeChecker(y: List[str]) -> bool:
            #remove the '.' as they are not numbers
            filtered = [i for i in y if i != '.']
            return len(filtered) == len(set(filtered))
        
        #check each condition:
        #condition 1: Each row must contain the digits 1-9 without duplicates.
        for y in board:
            if not dupeChecker(y):
                return False
        
        #condition 2: Each column must contain the digits 1-9 without duplicates.
        temp = [[],[],[],[],[],[],[],[],[]]

        #populate the temp board with column list
        for y in range(len(board)):
            index = 0
            for x in board[y]:
                temp[index].append(x)
                index += 1
        
        for y in temp:
            if not dupeChecker(y):
                return False
        
        #condition 3: Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
        temp = [[],[],[],[],[],[],[],[],[]]

        #Populate temp board with values from each 3x3 sub-box
        for i in range(3):
            for j in range(3):
                #Determine which sub-box were in (0 to 8)
                """When i and j range over 0, 1, 2 (from the starting points of each 3x3 block), box_index will yield a unique value from 0 to 8 for each sub-box.
                Top-left sub-box (start at (0,0)) has box_index = 0 * 3 + 0 = 0.
                Middle sub-box in the top row (start at (0,3)) has box_index = 0 * 3 + 1 = 1.
                Middle-right sub-box in the bottom row (start at (6,6)) has box_index = 2 * 3 + 2 = 8.
                """
                box_index = i * 3 + j
                #Each 3x3 sub-box contains values in the rows and columns i * 3 to i * 3 + 2 and j * 3 to j * 3 + 2.
                for row in range(i * 3, i * 3 + 3):
                    for col in range(j * 3, j * 3 + 3):
                        temp[box_index].append(board[row][col])
                
        for y in temp:
            if not dupeChecker(y):
                return False

        return True
        

