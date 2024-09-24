class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [] #list to add output to in spiral order

        #indexs for iterating over the matrix
        xBeg = 0 
        xEnd = len(matrix[0]) - 1
        yBeg = 0
        yEnd = len(matrix) - 1

        #base case: begining and end values equal each other(ie. arrive at center value in matrix)
        while xBeg <= xEnd and yBeg <= yEnd:
            #order of spiral is right, down, left, up
            #right (the y value stays the same while x value increases)
            for x in range(xBeg, xEnd + 1):
                result.append(matrix[yBeg][x])

            #update y value to go down 1 row:
            yBeg += 1

            #down (x value stays the same while y value decreases)
            for y in range(yBeg, yEnd + 1):
                result.append(matrix[y][xEnd])

            #update xEnd value to go down by 1 as you now start at the second to last x value
            xEnd -= 1

            #left(y value stays same while x value decreases)
            if yBeg <= yEnd: #check because if the above too move to a matrix already covered t he while loop wont catch until after all for loops
                for x in range(xEnd, xBeg -1, -1): #start, stop at last value, step is decrease 1
                    result.append(matrix[yEnd][x]) #yEnd because u want the bottom row
            
                #update yEnd to go down by 1 as that row has been finished
                yEnd -= 1

            #Up (x value stays same while y value decreases)
            if xBeg <= xEnd:
                for y in range(yEnd, yBeg -1, -1):
                    result.append(matrix[y][xBeg])
                
                #update X beginning value by 1 as that column has been completed
                xBeg += 1

        return result
            

                    