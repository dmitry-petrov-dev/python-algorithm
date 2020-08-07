# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
# значения.
from random import randint

result = -1
array_1 = [randint(-100, 10) for _ in range(0, 10)]
print(array_1)

for index, el in enumerate(array_1):
    if el < 0 and result == -1:
        result = index
    elif 0 > el > array_1[result]:
        result = index
print(f'Max negative value {array_1[result]}; position {result + 1},')
