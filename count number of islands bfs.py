class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time complexity is O(m*n) 
        Space complexity: visit is O(M*N), queue is O(min(m,n)), visit is dominating factor so overall space complexity is O(M*N)
        
        """
        if not grid: #empty grid
            return 0
        
        rows, cols = len(grid), len(grid[0]) #get rows and columns of matrix (MEMORIZE)
        visit = set() 
        islands = 0 #want to return islands

        def bfs(row,col):
            q = collections.deque() #bfs uses a queue FIFO (first in, first out)
            visit.add((row,col)) #add intial starting coordinate to the visit set
            q.append((row, col)) #add the starting point to the queue as well

            while q: #while the queue isnt empty
                row, col = q.popleft() #remove the current coordinate as it has been explored (added to visit)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] #these are the (row, col) directions you can travel (neighboring cells to see if they are 1s)

                for dr, dc in directions: #check all four possible neighbors of current cord
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < rows and 0 <= new_col < cols  #Check for boundaries 
                        and grid[new_row][new_col] == '1'  # Is land
                        and (new_row, new_col) not in visit  # Not visited
                    ):
                        q.append((new_row, new_col)) #if its an island add it to the q for further exporation on the next loop
                        visit.add((new_row, new_col))  # Mark as visited

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visit:
                    bfs(row,col) #check for connected islands
                    islands += 1 #increment island count by 1 and if you traverse a coordinate on the island it will already be in visit

        return islands