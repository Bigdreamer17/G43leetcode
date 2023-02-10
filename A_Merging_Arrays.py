n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
s = []

ptr1 = ptr2 = 0

while ptr1 < n or ptr2 < m:
    if ptr2 == m or ptr1 < n and num1[ptr1] < num2[ptr2]:
        s.append(num1[ptr1])
        ptr1 += 1
    else:
        s.append(num2[ptr2])
        ptr2 += 1
print(*s)