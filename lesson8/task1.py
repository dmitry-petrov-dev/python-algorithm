# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
from random import randint

counter = 0

# Подготавливаем граф:
# 0 - там где тот же человек
# 1 - рукопожатие со всеми
n = randint(1, 10)
graph = [[1] * n for i in range(n)]
for i in range(0, len(graph)):
    graph[i][i] = 0

print(f"Количество друзей: {n}")
print(f"Граф рукопожатий:")
for i, line in enumerate(graph):
    for j, item in enumerate(line):
        print(f'{item:>4}', end='')
        # считаем только то, что выше диагонали, чтобы учесть рукопожатие 1 раз.
        if j > i:
            counter += 1
    print()
print(f'Количество рукопожатий: {counter}')
