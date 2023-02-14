n , m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = []
ptr1 = 0
    
for ptr2 in range(m):
        while ptr1 < n and arr2[ptr2] > arr1[ptr1]:
            ptr1 += 1
        ans.append(ptr1)
        
print(*ans)