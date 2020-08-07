# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел
# из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
# несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом.

from collections import deque, namedtuple


def hex_sum(hex1, hex2):
    # The sum of the two hex numbers

    if len(hex1) > len(hex2):
        hex1, hex2 = deque(hex1), deque(hex2)
    else:
        hex1, hex2 = deque(hex2), deque(hex1)
    rank = 0
    result = deque()
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while hex1:
        if hex2:
            spam = hex_dict[hex1.pop()] + hex_dict[hex2.pop()] + rank
        else:
            spam = hex_dict[hex1.pop()] + rank

        if spam > 15:
            spam = spam % 16
            rank = 1
        else:
            rank = 0
        if spam >= 10:
            spam = hex_dict[spam]
        result.appendleft(str(spam))

    if rank:
        result.appendleft('1')
    return result


def hex_mult(hex1, hex2):
    # The multiplication of the two hex numbers:

    if len(hex1) > len(hex2):
        hex1, hex2 = deque(hex1), deque(hex2)
    else:
        hex1, hex2 = deque(hex2), deque(hex1)
    hex1.reverse()  # reverse
    rank = 0
    spam1 = deque([deque() for _ in range(len(hex2))])
    result = deque()
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    for i in range(len(hex2)):
        num = hex_dict[hex2.pop()]
        for j in range(len(hex1)):
            spam1[i].append(num * hex_dict[hex1[j]])
        spam1[i].reverse()  # reverse
        for j in range(i):
            spam1[i].append(0)
    for i in range(len(spam1[-1])):
        spam2 = rank
        for j in range(len(spam1)):
            if spam1[j]:
                spam2 += spam1[j].pop()
        if spam2 > 15:
            rank = spam2 // 16
        else:
            rank = 0
        spam2 = spam2 % 16
        if spam2 >= 10:
            spam2 = hex_dict[spam2]
        result.appendleft(str(spam2))
    if rank:
        if rank >= 10:
            rank = hex_dict[rank]
        result.appendleft(str(rank))
    return result


first = list(input("Введите первое HEX-число: ").upper())
second = list(input("Введите второе HEX-число: ").upper())
print(f"Результат сложения: {''.join(hex_sum(first, second))}")
print(f"Результат умножения: {''.join(hex_mult(first, second))}")
