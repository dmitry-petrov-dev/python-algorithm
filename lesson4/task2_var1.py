# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

import cProfile


# алгоритм «Решето Эратосфена».
def eratosthenes(n):
    size = 20 * n
    sieve = [_ for _ in range(size)]
    sieve[1] = 0
    j = 0
    while True:
        for i in range(2, size):
            if sieve[i] != 0:
                j += 1  # prime counter
                if j == n:
                    return sieve[i]
                k = i * 2
                while k < size:
                    sieve[k] = 0
                    k += i

# cProfile.run('eratosthenes(10000)')

# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(10)"
# 1000 loops, best of 3: 22.2 usec per loop
# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(100)"
# 1000 loops, best of 3: 312 usec per loop
# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(1000)"
# 1000 loops, best of 3: 4.55 msec per loop
# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(10000)"
# 1000 loops, best of 3: 111 msec per loop

# cProfile.run('eratosthenes(10)')
# task2_var1.py
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2_var1.py:3(eratosthenes)
#         1    0.000    0.000    0.000    0.000 task2_var1.py:5(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('eratosthenes(100)')
# task2_var1.py
#          5 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 task2_var1.py:3(eratosthenes)
#         1    0.000    0.000    0.000    0.000 task2_var1.py:5(<listcomp>)
#         1    0.001    0.001    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('eratosthenes(1000)')
# task2_var1.py
#          5 function calls in 0.019 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#         1    0.013    0.013    0.019    0.019 task2_var1.py:3(eratosthenes)
#         1    0.006    0.006    0.006    0.006 task2_var1.py:5(<listcomp>)
#         1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('eratosthenes(10000)')
# task2_var1.py
#          5 function calls in 0.342 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.005    0.005    0.342    0.342 <string>:1(<module>)
#         1    0.278    0.278    0.337    0.337 task2_var1.py:3(eratosthenes)
#         1    0.058    0.058    0.058    0.058 task2_var1.py:5(<listcomp>)
#         1    0.000    0.000    0.342    0.342 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
