# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())

ans = True
for i in range(n):
    B = set(input().split())
    if len(A.difference(B)) == 0 or len(B.difference(A)) >= 1:
        ans = False

print(ans)
