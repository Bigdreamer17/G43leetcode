def countSwaps(a):
    # Write your code here
    cont = 0
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                cont += 1
    print("Array is sorted in", str(cont) ,"swaps.")
    print("First Element:" , a[0])
    print("Last Element:", a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)