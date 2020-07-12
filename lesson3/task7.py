# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба минимальны), так и различаться.
from random import randint

array_1 = [randint(0, 1000) for _ in range(0, 15)]
print(f"Array: {array_1}")

min1 = array_1[0]
min2 = array_1[0]

for el in array_1[1:]:
    if el < min1:
        min2, min1 = min1, el
    elif el < min2:
        min2 = el

print(f"Minimum1 - {min1}, Minimum2 - {min2}")
