# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

# init result list
result = [0 for _ in range(2, 10)]

for num in range(2, 100):
    for comp_num in range(2, 10):
        if num % comp_num == 0:
            result[comp_num - 2] += 1

for comp_num in range(2, 10):
    print(f"Number {comp_num} - {result[comp_num - 2]}")
