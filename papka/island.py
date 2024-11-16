import random

def generate_island_matrix(rows, cols):
    """Генерирует матрицу с одним островом, где 1 - суша, а 0 - вода."""
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Остров не должен располагаться на краю карты
    start_row = random.randint(1, rows - 2)
    start_col = random.randint(1, cols - 2)

    # Начинаем с одной точки суши
    matrix[start_row][start_col] = 1
    island_size = random.randint(5, (rows - 2) * (cols - 2) // 4)  # Произвольный размер острова
    cells_to_fill = [(start_row, start_col)]

    # Разрастаем остров, добавляя соседние ячейки
    while len(cells_to_fill) < island_size:
        r, c = random.choice(cells_to_fill)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 1 <= nr < rows - 1 and 1 <= nc < cols - 1 and matrix[nr][nc] == 0:
                matrix[nr][nc] = 1
                cells_to_fill.append((nr, nc))
                break

    return matrix, len(cells_to_fill)

def set_heights(matrix):
    """Устанавливает высоты клеток на острове согласно заданным правилам."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    heights = [[0 for _ in range(cols)] for _ in range(rows)]

    # Находим координаты всех клеток суши
    land_cells = [(r, c) for r in range(rows) for c in range(cols) if matrix[r][c] == 1]

    # Определяем центр острова
    if land_cells:
        center_row = sum(r for r, c in land_cells) // len(land_cells)
        center_col = sum(c for r, c in land_cells) // len(land_cells)

    # Устанавливаем высоты
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:  # Если это суша
                distance_to_center = max(abs(r - center_row), abs(c - center_col))
                heights[r][c] = max(1, min(4, 4 - distance_to_center))  # Высота суши
            else:  # Если это вода
                # Проверяем соседние клетки для определения глубины
                if any(0 <= r + dr < rows and 0 <= c + dc < cols and matrix[r + dr][c + dc] == 1
                       for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    heights[r][c] = 0  # Глубина 0, если рядом с сушей
                else:
                    heights[r][c] = -1  # Глубина отрицательная, если далеко от суши

    return heights

def calculate_perimeter(matrix):
    """Вычисляет периметр острова."""
    perimeter = 0
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:  # Если это суша
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or matrix[nr][nc] == 0:
                        perimeter += 1  # Увеличиваем периметр

    return perimeter

def print_matrix(matrix):
    """Выводит матрицу в удобочитаемом формате."""
    for row in matrix:
        print(' '.join(str(cell) for cell in row))

# Пример использования
rows = int(input("Введите количество строк (минимум 5): "))
cols = int(input("Введите количество столбцов (минимум 5): "))
matrix, island_area = generate_island_matrix(rows, cols)
island_heights = set_heights(matrix)
print_matrix(island_heights)
island_perimeter = calculate_perimeter(matrix)
print(f"Периметр: {island_perimeter}")
print(f"Площадь: {island_area}")
