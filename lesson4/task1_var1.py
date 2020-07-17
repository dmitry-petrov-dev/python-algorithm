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
    if n == 0:
        return even, odd
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    return func_calc(n // 10, even, odd)

# cProfile.run('func_calc(2**4000)')

# 2**10
# 1000 loops, best of 3: 0.659 usec per loop
# 2**100
# 1000 loops, best of 3: 12 usec per loop
# 2**1000
# 1000 loops, best of 3: 221 usec per loop
# 2**2000
# 1000 loops, best of 3: 729 usec per loop
# 2**3000
# 1000 loops, best of 3: 1.53 msec per loop
# 2**4000
# RuntimeError: maximum recursion depth exceeded in cmp

# 2**10
# 5/1    0.000    0.000    0.000    0.000 task1_var1.py:4(func_calc)
# 2**100
# 32/1    0.000    0.000    0.000    0.000 task1_var1.py:4(func_calc)
# 2**1000
# 303/1    0.000    0.000    0.000    0.000 task1_var1.py:4(func_calc)
# 2**2000
# 604/1    0.001    0.000    0.001    0.001 task1_var1.py:4(func_calc)
# 2**3000
# 905/1    0.002    0.000    0.002    0.002 task1_var1.py:4(func_calc)
# 2**4000
# RecursionError: maximum recursion depth exceeded in comparison
