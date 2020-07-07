# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def func_calc(n, even, odd):
    if n == 0:
        return f'Количество четных цифр: {even}\nКоличество нечетных цифр: {odd}'
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    return func_calc(n // 10, even, odd)


num = 1234567890
print(func_calc(num, 0, 0))