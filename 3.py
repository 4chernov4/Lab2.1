def sum_diagonal(matrix):
    s = 0
    for i in range(len(matrix)):
        s += matrix[i][i]
    return s

matrix = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

s = sum_diagonal(matrix)

print(s)
