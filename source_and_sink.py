n = int(input())
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = []
sink = []


for i in range(n):
    ones_r = 0
    for j in range(n):
        if graph[i][j] == 1:
            ones_r += 1
            break
    if ones_r == 0:
        source.append(i + 1)


for i in range(n):
    ones_c = 0
    for j in range(n):
        if graph[j][i] == 1:
            ones_c += 1
            break

    if ones_c == 0:    
        sink.append(i + 1)

print(len(sink), *sink)
print(len(source), *source)
