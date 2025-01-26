class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set() , set() #subsets for each coordinate that can reach pacific or atlantic ocean

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r == ROWS or r < 0 or c == COLS or c < 0 or heights[r][c] < prevHeight): #base cases
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) #top row for pacific
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])  #bottom row for atlantic

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) #most left colum for pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) #most right column for atlantic
        
        res= []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])
        
        return res