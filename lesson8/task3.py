# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import randint


def graph_gen(vertex):
    v = set()
    g = dict()
    for i in range(0, vertex):
        v = set()
        for j in range(0, vertex):
            direct = randint(0, 1)
            if i != j and direct > 0:
                v.add(j)
        g[i] = v
    return g


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for item in graph[start] - visited:
        dfs(graph, item, visited)
    return visited


graph = graph_gen(10)
print(f'Сгенерированый граф: {graph}')
print('Обход вершин:')
visited_vertex = dfs(graph, 0)
print()
print(f'Посещенные вершины: {visited_vertex}')