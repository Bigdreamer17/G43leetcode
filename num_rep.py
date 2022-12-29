def Replacement(array, word):
    dictionary = {}
    for key in array:
        for value in word:
            if key in dictionary and dictionary[key] != value:
                return False
            dictionary[key] = value
    return True

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = input()

if Replacement(arr, s):
    print("Yes")
else:
    print("No")
