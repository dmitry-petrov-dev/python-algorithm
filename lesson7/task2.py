# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


size = 100
array = [random.uniform(0, 50) for _ in range(size)]
random.shuffle(array)
print("Initial array:")
print(array)
print("*" * 30)
print("Sorted array:")
print(merge_sort(array))
