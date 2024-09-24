"""
Conditions:
Both matrices must have the same number of rows.
Both matrices must have the same number of columns.
"""
def add_matrices(matrix1, matrix2):
    #Check if the dimensions are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]): #len(matrix1) is the 'row' length (ie. how many nested lists there are) and len(matrix1[0]) gives the number of columns
        raise ValueError("Matrices must have the same dimensions to be added.")
    
    result = [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] #add corresponding values in the same row for the number of columns
        for i in range(len(matrix1)) #do above code for all the rows (outer for loop it technically executes first)
    ]
    return result

matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

result = add_matrices(matrix1, matrix2)
print(result)  # Output: [[6, 8], [10, 12]]

#error example
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6, 7],
    [8, 9, 10]
]

#This will raise an error
result = add_matrices(matrix1, matrix2)