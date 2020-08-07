# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


def bubble_sort(array):
    for j in range(1, len(array)):
        flag = False
        for i in range(len(array) - j):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
        if not flag:  # already sorted
            break
    return array


size = 50
array = [random.randint(-100, 99) for _ in range(size)]
random.shuffle(array)
print("Initial array:")
print(array)
print("*" * 30)
print("Sorted array:")
print(bubble_sort(array))
