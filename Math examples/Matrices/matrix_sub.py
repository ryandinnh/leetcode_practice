def subtract_matrices(matrix1, matrix2):
    #Check if the dimensions are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to be subtracted.")
    
    result = [
        [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]#nested loop executed second
        for i in range(len(matrix1))#outer loop executes first
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

result = subtract_matrices(matrix1, matrix2)
print(result)  #Output: [[-4, -4], [-4, -4]]
