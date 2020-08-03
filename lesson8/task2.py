# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
# необходимо обойти.
from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    ss = start  # исходная вершина
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    # вывод списка с вершинами и итоговый вес
    ways = []
    for i in range(length):
        if i == ss:
            ways.append(ss)
        elif parent[i] == -1:
            ways.append('нет пути')
        if i != ss and parent[i] != -1:
            way = deque([i])
            j = i
            while parent[j] != ss:
                way.appendleft(parent[j])
                j = parent[j]
            way.appendleft(ss)
            ways.append(list(way))
    return ways, cost


s = int(input('От какой вершины идти: '))
ways, cost = dijkstra(g, s)
for i in range(0, len(cost)):
    print(f"Путь: {ways[i]}, вес: {cost[i]}")
