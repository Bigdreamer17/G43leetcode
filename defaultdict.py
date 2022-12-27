# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = list(map(int, input().split()))

d = defaultdict(list)
for i in range(n):
    d[input()].append(i + 1)
for _ in range(m):
    search = d[input()]
    if search == []:
        print(-1)
    else:
        print(' '.join(map(str, search)))
