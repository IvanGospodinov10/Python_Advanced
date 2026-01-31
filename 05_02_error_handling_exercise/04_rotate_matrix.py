class MatrixContentError(Exception):
    """Verify the matrix contains only integers"""
    pass


class MatrixSizeError(Exception):
    """Ensure the input is an N x N (2D matrix),"""
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()

    if not line:
        break

    for el in line:
        if not el.isdigit():
            raise MatrixContentError("The matrix must consist of only integers")

    mtrx.append(line)

matrix_len = len(mtrx)
for row in mtrx:
    if len(row) != matrix_len:
        raise MatrixSizeError("TThe size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
