import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        going to want to traverse grid matrix
        use BFS but return number of 1s traverse

        time and space complexity is O(m*n)

        """
        area = 0
        visit = set() #hashset to keep track of visited cords going to include (row, col) tuples
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c) -> int:
            q = collections.deque() #FIFO 
            visit.add((r, c))  #key remember we are adding as tuples
            q.append((r, c))
            a = 1 #current island area

            while q: #while there are still islands with 1
                row, col = q.popleft() #pop start of queue as explored
                #directions we can go next
                directions = [[0,1], [0,-1], [1,0], [-1,0]]

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    #conditions for an island:
                    if (0 <= newRow < rows and 0 <= newCol < cols #boundary check to make sure we are still in grid use max rows and cols value
                        and grid[newRow][newCol] == 1 #check if new cord is an island
                        and (newRow, newCol) not in visit): #check if coordinate has already been traversed
                        #if it is a valid island add it to visited and add it to q to explore its neighbord next
                        a += 1
                        visit.add((newRow, newCol)) 
                        q.append((newRow, newCol))
                        
                
            return a 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit: #need to make sure the coordinate hasnt already been traversed
                    area = max(area, bfs(r, c)) 
        
        return area