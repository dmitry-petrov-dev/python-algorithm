# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с
# кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# **********************************************************************************************************************
# Задание 3.9.
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# 3.6.9 (default, Jul 17 2020, 12:50:27)
# [GCC 8.4.0] linux 64-bit
# **********************************************************************************************************************

import sys

from random import randint


def show_size(x, level=0):
    x_size = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                x_size += show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                x_size += show_size(xx, level + 1)
    return x_size


def show_total_size(*args):
    memory = 0
    for x in args:
        memory += show_size(x)
    return memory


# Generate matrix
size = 5
matrix = tuple([[randint(1, 100) for _ in range(size)] for _ in range(size)])
print(f"Matrix {size}x{size} = ")
min_column = []
min_column.extend(matrix[0])
for line in matrix:
    for index, item in enumerate(line):
        if item < min_column[index]:
            min_column[index] = item
        print(f'{item:>4}', end='')
    print()

print(f"\nList of minimum values by columns: {min_column}")
min_column.sort(reverse=True)
print(f"Maximum - {min_column[0]}")
print()
print('Total memory: ')
print(f'{show_total_size(size, matrix, min_column, line, index, item)}')
# Total memory = 2048
