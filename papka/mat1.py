import random
x, y = list(map(int, input("Введите размерности матрицы: ").split()))
matrix = [[random.randint(0, 1000) for i in range(x)] for j in range(y)]
for i in range(len(matrix)):
    matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
for i in range(len(matrix)):
    print(*matrix[i])
