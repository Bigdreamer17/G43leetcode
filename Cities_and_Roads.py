from collections import defaultdict

n = int(input())
graph = defaultdict(list) 
matrix = []

for _ in range(n):
    Rows = list(map(int, input().split()))
    matrix.append(Rows)


ones = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            ones += 1

print(ones // 2)