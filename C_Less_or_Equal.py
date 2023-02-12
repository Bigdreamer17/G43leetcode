size, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
if k == 0:
    ans =  nums[0] - 1
else:
    ans = nums[k - 1]
cnt = 0
for i in nums:
    if i <= ans:
        cnt += 1
if ans < 1 or cnt != k:
    print(-1)
else:
    print(ans)