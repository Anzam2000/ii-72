import random
def create_empty_matrix(size):
    return [[random.randint(-3, 0) for _ in range(size)] for _ in range(size)]
def add_large_island(matrix, start_x, start_y, island_size):
    height_values = random.sample(range(1, 6), 5)
    count = 0
    for x in range(start_x, start_x + island_size):
        for y in range(start_y, start_y + island_size):
            if x < len(matrix) and y < len(matrix[0]):
                matrix[x][y] = height_values[count % 5] 
                count += 1
def calculate_perimeter(matrix):
    perimeter = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] > 0:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or matrix[nx][ny] <= 0:
                        perimeter += 1
    return perimeter
def calculate_area(matrix):
    area = 0
    for row in matrix:
        for cell in row:
            if cell > 0: 
                area += 1
    return area
def generate_island(size):
    matrix = create_empty_matrix(size)
    start_x = size // 4  
    start_y = size // 4 
    island_size = size // 2 
    add_large_island(matrix, start_x, start_y, island_size)
    return matrix


def print_island(matrix):
    for row in matrix:
        print(' '.join(str(cell) for cell in row))
    print()


# Параметры
size = 20  # Размер матрицы

# Генерация и вывод острова
island = generate_island(size)
print_island(island)

# Вычисляем периметр и площадь
perimeter = calculate_perimeter(island)
area = calculate_area(island)
print(f"Периметр острова: {perimeter}")
print(f"Площадь острова: {area}")
