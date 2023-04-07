from collections import defaultdict

n = int(input())
matrix = []

for i in range(n):
    rows = list(map(int, input().split()))
    matrix.append(rows)

graph = defaultdict(list)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i].append(j + 1)
for values in graph.values():
    print(len(values), *values)

