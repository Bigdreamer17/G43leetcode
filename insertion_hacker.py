def insertionSort1(n, arr):
    # Write your code here
    target = arr[-1]
    idx = n-2

    while (target < arr[idx]) and (idx >= 0):
        arr[idx+1] = arr[idx]
        print(*arr)
        idx -= 1

    arr[idx+1] = target
    print(*arr)