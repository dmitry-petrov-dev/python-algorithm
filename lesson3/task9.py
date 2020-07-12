# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

# Generate matrix
size = 5
matrix = [[randint(1, 100) for _ in range(size)] for _ in range(size)]
# Initialize list of minimum values
min_column = []
min_column.extend(matrix[0])
print(f"Matrix {size}x{size} = ")
for line in matrix:
    for index, item in enumerate(line):
        if item < min_column[index]:
            min_column[index] = item
        print(f'{item:>4}', end='')
    print()

max_element = min_column[0]
for item in min_column[1:]:
    if max_element < item:
        max_element = item
print(f"\nList of minimum values by columns: {min_column}")
print(f"Maximum - {max_element}")
