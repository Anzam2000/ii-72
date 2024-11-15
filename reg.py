import random
matrix = [[random.randint(-9, 9) for _ in range(10)] for _ in range(10)]
for row in matrix:
    print('\t'.join(map(str, row)))
n = len(matrix)
for i in range(n):
    matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]
print('Новая матрица:')
for row in matrix:
    print('\t'.join(map(str, row)))
diagonal_elements = []
for i in range(n):
    diagonal_elements.append(matrix[i][i])
    diagonal_elements.append(matrix[i][n - 1 - i])
max_diagonal_value = max(diagonal_elements)
print('Максимальное число из диагоналей:', max_diagonal_value)
