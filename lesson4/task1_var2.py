# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили
# замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import cProfile


def func_calc(n, even=0, odd=0):
    even = 0
    odd = 0
    for f in str(n):
        i = int(f)
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

# cProfile.run('func_calc(2**4000)')

# 2**10
# 1000 loops, best of 3: 1.63 usec per loop
# 2**100
# 1000 loops, best of 3: 12.3 usec per loop
# 2**1000
# 1000 loops, best of 3: 109 usec per loop
# 2**2000
# 1000 loops, best of 3: 266 usec per loop
# 2**3000
# 1000 loops, best of 3: 390 usec per loop
# 2**4000
# 1000 loops, best of 3: 429 usec per loop
# 2**10000
# 1000 loops, best of 3: 1.24 msec per loop