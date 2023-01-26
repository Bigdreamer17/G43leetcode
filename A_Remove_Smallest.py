test_case =int(input())
for _ in range(test_case):
    size = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    for i in range(size - 1):
        if arr[i + 1] - arr[i] > 1:
            print("NO")
            break
    else: 
        print("YES")
    