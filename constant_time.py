A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
B = [
    [17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32]
]

def add_matrices(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract_matrices(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2
    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bottom_left = [row[:mid] for row in matrix[mid:]]
    bottom_right = [row[mid:] for row in matrix[mid:]]
    return top_left, top_right, bottom_left, bottom_right

def combine_matrices(C11, C12, C21, C22):
    n = len(C11) * 2
    C = [[0] * n for _ in range(n)]
    mid = n // 2
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C

def divide_and_conquer_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    
    M1 = divide_and_conquer_multiply(A11, B11)
    M2 = divide_and_conquer_multiply(A12, B21)
    M3 = divide_and_conquer_multiply(A11, B12)
    M4 = divide_and_conquer_multiply(A12, B22)
    M5 = divide_and_conquer_multiply(A21, B11)
    M6 = divide_and_conquer_multiply(A22, B21)
    M7 = divide_and_conquer_multiply(A21, B12)
    M8 = divide_and_conquer_multiply(A22, B22)
    
    C11 = add_matrices(M1, M2)
    C12 = add_matrices(M3, M4)
    C21 = add_matrices(M5, M6)
    C22 = add_matrices(M7, M8)
    
    return combine_matrices(C11, C12, C21, C22)

result = divide_and_conquer_multiply(A, B)
for row in result:
    print(row)





