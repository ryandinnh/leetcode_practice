def multiply_matrices(A, B):
    #Number of rows in A
    rows_A = len(A)
    #Number of columns in A
    cols_A = len(A[0])
    # Number of rows in B
    rows_B = len(B)
    #Number of columns in B
    cols_B = len(B[0])

    # Check if matrix dimensions are compatible for multiplication
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")
    
    #Initialize the result matrix with zeros (resulting matrix will be rows from A and columns from B)
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    #Perform the matrix multiplication (dot products)
    for i in range(rows_A): 
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j] #row value from A x column value from B(Matrix A will keep going across while Matrix B goes down)
    
    return result

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply_matrices(A, B)
print(result)  # Output: [[58, 64], [139, 154]]
