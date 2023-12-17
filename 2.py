def swap(matrix, col1, col2):
    for row in matrix:
        row[col1], row[col2] = row[col2], row[col1]

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

print("Исходная матрица:")
print_matrix(matrix)

column_index1 = 3
column_index2 = 4

swap(matrix, column_index1, column_index2)

print("Матрица после перестановки столбцов:")
print_matrix(matrix)
