# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.

import hashlib


def calc_substring(s: str, dbg=False):
    len_string = len(s)

    assert len_string != 0, 'Строка не может быть пустой'

    h_subs = set()
    for ind in range(len_string):
        for i in range(ind, len_string):
            h_subs.add(hashlib.sha1(s[ind:i + 1].encode('utf-8')).hexdigest())
    h_subs.remove(hashlib.sha1(s.encode('utf-8')).hexdigest())  # исключаем хеш самой строки
    if dbg:  # для дэбага
        print('Хэши подстрок: ')
        print(h_subs)
    return len(h_subs)


debug = False
if debug:
    str_line = ''
    print(f'Количество различных подстрок в строке: {calc_substring(str_line, debug)}')
    str_line = 'beep boop beer boop'
    print(f'Количество различных подстрок в строке: {calc_substring(str_line, debug)}')

str_line = input('Введите строку: ')
print(f'Количество различных подстрок в строке: {calc_substring(str_line)}')
