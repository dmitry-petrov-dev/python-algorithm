# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = input("Введите первую букву: ")
b = input("Введите вторую букву: ")

seqn_a = ord(a) - ord('a') + 1
seqn_b = ord(b) - ord('a') + 1
qty_chars = abs(seqn_a - seqn_b)
if qty_chars >= 1:
    qty_chars -= 1
else:
    qty_chars = 0
print(f"Позиция буквы {a} в алфавите {seqn_a}")
print(f"Позиция буквы {b} в алфавите {seqn_b}")
print(f"Количество букв между {a} и {b}: {qty_chars}")
