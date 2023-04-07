from collections import defaultdict
graph = defaultdict(list)

def add_edge(origin, destination):
    graph[origin].append(destination)
    graph[destination].append(origin)

def print_vetrtice(origin):
    ans = graph[origin]
    print(*ans)

vertices = int(input())
operations = int(input())

for _ in range(operations):
    op = list(map(int, input().split()))
    if op[0] == 1:
        add_edge(op[1], op[2])
    if op[0] == 2:
        print_vetrtice(op[1])




