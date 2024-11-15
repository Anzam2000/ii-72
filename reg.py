import random

matrix = [[random.randint(0, 1) for _ in range(10)] for _ in range(10)]
for row in matrix:
    print('\t'.join(map(str, row)))
for row in matrix:
    row[0], row[-1] = row[-1], row[0]
for row in matrix:
    print(*row)
