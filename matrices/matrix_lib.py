### Matrix Lib ###


def vector_dot_product(vectorA, vectorB):
    dp = 0
    if len(vectorA) == len(vectorB):
        for i in range(len(vectorA)):
                dp += vectorA[i] * vectorB[i]

    return dp


def transpose(matrix):
    new_matrix = [
            [ matrix[j][i] for j in range(len(matrix)) ]
            for i in range(len(matrix[0]))
    ]

    return new_matrix


def identity_matrix(n):
    identity = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)

        identity.append(row)

    return identity


def matrix_addition(matrixA, matrixB):

    # initialize matrix to hold the results
    matrixSum = []

    # matrix to hold a row for appending sums of each element
    row = []

    # TODO: write a for loop within a for loop to iterate over
    # the matrices

    # TODO: As you iterate through the matrices, add matching
    # elements and append the sum to the row variable

    # TODO: When a row is filled, append the row to matrixSum.
    # Then reinitialize row as an empty list
    for i in range(len(matrixA)):
        row = []

        if isinstance(matrixA[i], list):
            for j in range(len(matrixA[i])):
                A = matrixA[i][j]
                B = matrixB[i][j]
                row.append(A+B)

            matrixSum.append(row)
        else:
            matrixSum.append(matrixA[i] + matrixB[i])

    return matrixSum


def matrix_multiplication(matrixA, matrixB):
    product = []
    matrixB_T = transpose(matrixB)
    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB_T)):
            dp = vector_dot_product(matrixA[i], matrixB_T[j])
            row.append(dp)

        product.append(row)

    return product


def inverse_matrix(matrix):

    inverse = []

    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix must be square')

    ## TODO: Check if matrix is larger than 2x2.
    ## If matrix is too large, then raise an error
    side_length = len(matrix)
    if side_length > 2:
        raise ValueError('The matrix must smaller than 2x2')

    ## TODO: Check if matrix is 1x1 or 2x2.
    ## Depending on the matrix size, the formula for calculating
    ## the inverse is different

    ## TODO: Calculate the inverse of the square 1x1 or 2x2 matrix.
    if side_length == 1:
        inverse.append([1/matrix[0][0]])

    elif side_length ==2:
        #[a b]^-1
        #[c d]

        #=

        #1/(ad-bc) *
        #[d -b]
        #[-c a]

        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]

        inverse_determinant = 1/(a*d - b*c)

        traceAI_minusA = [ [d, -b],
                           [-c, a] ]

        for i in range(len(traceAI_minusA)):
            row = []
            for j in range(len(traceAI_minusA[i])):
                row.append(inverse_determinant * traceAI_minusA[i][j])
            inverse.append(row)

    return inverse



A = [
    [2,5,1],
    [6,9,7.4],
    [2,1,1],
    [8,5,3],
    [2,1,6],
    [5,3,1]
]

B = [
    [7, 19, 5.1],
    [6.5,9.2,7.4],
    [2.8,1.5,12],
    [8,5,3],
    [2,1,6],
    [2,33,1]
]

print("Vector dot product")
print(vector_dot_product([1,2,3], [4,5,6]), "  (32?)\n")

print("Transpose")
print(transpose(A), "\n")


print("Identity")
print(identity_matrix(1))
print(identity_matrix(3), "\n")

print("Addition")
print(matrix_addition(A, B), "\n")

# 6x3 * 3x6 should equal 6x6
print("Multiplication")
print(matrix_multiplication( [[1,2]], [[3],[4]] ), " ([[11]]?)\n")
print("A  : ", A)
print("A*I: ", matrix_multiplication(A, identity_matrix(3)), "\n")
print("A*B_T: ", matrix_multiplication(A, transpose(B)), "\n")
