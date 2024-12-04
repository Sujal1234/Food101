def dot(array1, array2):
    if(not isinstance(array1[0], list)):
        #1d vectors
        return [x*y for x, y in zip(array1, array2)]
    result = []
    for row in range(len(array1)):
        vec = [x*y for x, y in zip(array1[row], array2[row])]
        result.append(vec)
    return result

def multipy(array1, array2):
    #m x n with n x p
    m = len(array1)
    n = len(array1[0])

    if(n != len(array2)):
        print("Invalid matrix multiplication!")
        return None
    p = len(array2[0])

    result = []
    for i in range(m):
        #m rows
        row = []
        for j in range(p):
            #multiply row i of array1 with column j of array2
            col = [array2[k][j] for k in range(n)]
            row.append(dot(col, array1[i]))
        result.append(row)

    return result

def get_submatrix(matrix, row, col):
    #gets submatrix excluding some row and column
    return [row_[:col] + row_[col+1:] for i, row_ in enumerate(matrix) if i != row]

def determinant(matrix):
    n = len(matrix)
    if(len(matrix[0]) != n):
        print("Not a square matrix!")
        return None

    if(n == 1):
        return matrix[0][0]

    det = 0
    for i in range(n):
        sign = -2*(i%2) + 1
        det += sign * determinant(get_submatrix(matrix, 0, i)) * matrix[0][i]
    return det


def matrix_operation(array1, array2, operation):
    if (operation == "dot"):
        return dot(array1, array2)

    elif (operation == "matrix"):
        return multiply(array1, array2)

    elif (operation == "determinant"):
        return (determinant(array1), determinant(array2))

    else:
        print("Inavlid operation!")

def get_user_inp():
    print("Enter your vectors/matrices in the form of a python list.")
    print("E.g. [1,2, 3] for a vector or [[1,2,3], [4, 5, 6]] for a matrix.")

    a = eval(input("Enter the first vector/matrix: "))
    b = eval(input("Enter the second vector/matrix: "))

    print("Enter the operation you want to perform between the vectors/matrices.")
    print("The available operations are: ")
    print("'dot' for dot product.")
    print("'matrix' for matrix multiplication.")
    print("'determinant' to calculate the determinant of the matrices.")

    op = input("Enter your operation: ")

    result = matrix_operation(a, b, op)
    if(not result is None):
        print("The result is:\n", result)

# matrix = [[1,2,3], [4,5,6], [7,8,9]]

# print(get_submatrix(matrix, 0, 1))
get_user_inp()
