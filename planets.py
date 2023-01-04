testcase = int(input())
for i in range(testcase):
    n, c = map(int, input().split())
    plantes = list(map(int, input().split()))
freq = {}
count = 0
for i in plantes:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for value in freq.values():
    if value >= c:
        count += c
    if value == 1:
        count += value
print(count)