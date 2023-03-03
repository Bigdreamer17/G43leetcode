t = int(input())
for i in range(t):
    a , b = map(int, input().split())

    ans = 0
    maxteam = (a + b) // 4

    ans += min(maxteam, min(a,b))

    print(ans)