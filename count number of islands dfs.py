class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time complexity is O(m*n) 
        Space complexity: visit is O(M*N), queue is O(min(m,n)), visit is dominating factor so overall space complexity is O(M*N)
        If you want to change to DFS its essentially the same you just recursively call DFS
        """
        if not grid: #empty grid
            return 0
        
        rows, cols = len(grid), len(grid[0]) #get rows and columns of matrix (MEMORIZE)
        visit = set() 
        islands = 0 #want to return islands

        def dfs(r, c):
            # Base case: mark the current cell as visited
            visit.add((r, c))

            # Directions to move in the grid (down, up, right, left)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            # Explore all four possible directions
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc

                # Check if the new cell is within the bounds of the grid, is land ('1'), and is unvisited
                if (
                    0 <= new_row < rows and 0 <= new_col < cols  # Boundary check
                    and grid[new_row][new_col] == '1'  # Check if it's land
                    and (new_row, new_col) not in visit  # Check if not visited
                ):
                    # Recursively perform DFS on the new cell
                    dfs(new_row, new_col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visit:
                    dfs(row,col) #check for connected islands
                    islands += 1 #increment island count by 1 and if you traverse a coordinate on the island it will already be in visit

        return islands