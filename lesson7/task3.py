# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
# другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


import random
import statistics

column_size = 5


def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam
    return array


def find_median(array):
    def select_pivot(array, i):
        length = len(array)
        if length <= column_size:
            return insertion_sort(array)[i]
        else:
            # split by column with size 5
            array_b = [select_pivot(k, (len(k) - 1) // 2) for k in
                       [array[j:(j + column_size)] for j in range(0, len(array), column_size)]]

            median = select_pivot(array_b, (len(array_b) - 1) // 2)

            left = [j for j in array if j < median]
            if i < len(left):
                return select_pivot(left, i)
            right = [j for j in array if j > median]
            right_length = len(right)
            if i < (length - right_length):
                return median
            return select_pivot(right, i - (length - right_length))

    return select_pivot(array, (len(array) - 1) // 2)


# Array size
size = 2 * random.randint(1, 50) + 1
# Array generation
array = [random.randint(0, size) for i in range(0, size)]
print(f"Generated array[{size}]:")
print(array)
print(f"Median of the array: {find_median(array)}")
print("*" * 30)
print("Sorted array:")
print(insertion_sort(array))
print(f"Checking result: {statistics.median(array)}")
