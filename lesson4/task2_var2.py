# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

import cProfile


# без использования «Решета Эратосфена»
def search_primes(n):
    def _search(_start, _finish):
        for i in range(_start, _finish + 1, 2):
            if (i > 10) and (i % 10 == 5):
                continue
            for k in prime[:]:
                if k * k - 1 > i:
                    prime.append(i)
                    break
                if i % k == 0:
                    break
            else:
                prime.append(i)
            if len(prime) == n:
                break
        return prime

    start = 3
    finish = n
    if n < 2:
        return 0
    prime = [2]
    while len(prime) < n:
        prime = _search(start, finish)
        start, finish = finish + 1, 4 * finish
    return prime[n - 1]

# cProfile.run('search_primes(10000)')
# print(search_primes(500))

# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(10)"
# 1000 loops, best of 3: 5.01 usec per loop
# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(100)"
# 1000 loops, best of 3: 118 usec per loop
# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(1000)"
# 1000 loops, best of 3: 2.65 msec per loop
# python -m timeit -n 1000 -s "import task2_var1" "task2_var1.eratosthenes(10000)"
# 1000 loops, best of 3: 84.1 msec per loop
#
# cProfile.run('search_primes(10)')
# task2_var2.py
#          30 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2_var2.py:4(search_primes)
#         2    0.000    0.000    0.000    0.000 task2_var2.py:5(_search)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        15    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('search_primes(100)')
# task2_var2.py
#          327 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2_var2.py:4(search_primes)
#         3    0.000    0.000    0.000    0.000 task2_var2.py:5(_search)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       221    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('search_primes(1000)')
# task2_var2.py
#          4178 function calls in 0.022 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.022    0.022 <string>:1(<module>)
#         1    0.000    0.000    0.022    0.022 task2_var2.py:4(search_primes)
#         3    0.022    0.007    0.022    0.007 task2_var2.py:5(_search)
#         1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
#      3172    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('search_primes(10000)')
# task2_var2.py
#          51902 function calls in 0.615 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.615    0.615 <string>:1(<module>)
#         1    0.000    0.000    0.614    0.614 task2_var2.py:4(search_primes)
#         3    0.609    0.203    0.614    0.205 task2_var2.py:5(_search)
#         1    0.000    0.000    0.615    0.615 {built-in method builtins.exec}
#     41896    0.004    0.000    0.004    0.000 {built-in method builtins.len}
#      9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
