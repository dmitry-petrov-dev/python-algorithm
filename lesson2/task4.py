# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры.

n = int(input("Введите количество элементов ряда: "))
a = 1
total = 0 if n <= 0 else a
while n > 1:
    a /= -2
    total += a
    n -= 1
print(f"Сумма элементов ряда равна: {total}")