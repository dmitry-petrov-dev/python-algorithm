# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

matrix = []

for line in range(5):
    total = 0
    matrix.append([])
    for column in range(3):
        num = int(input(f"Enter number for line {line + 1}, column {column + 1}: "))
        matrix[line].append(num)
        total += num
    matrix[line].append(total)

print("\nMatrix 5x4 = ")
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
