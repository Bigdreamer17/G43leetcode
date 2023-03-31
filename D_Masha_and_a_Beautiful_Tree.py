testCase = int(input())
def mergeSort(arr, start, end):
    if start == end:
        return [arr[start]]
    mid = (start + end) // 2

    left = mergeSort(arr, start, mid)
    right = mergeSort(arr, mid + 1, end)

    return merge(left, right)

count = 0
def merge(left, right): 
    global count 
    
    if left[0] <= right[0]:
        left.extend(right)
        return left
    else:
        count += 1
        right.extend(left)
        return right

for _ in range(testCase):
    count = 0

    size = int(input())
    nums = list(map(int, input().split()))
    arr = mergeSort(nums, 0, len(nums) - 1)
    
    if arr == sorted(arr):
        print(count)
    else:
        print(-1)