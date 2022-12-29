def Tsize(a, b):
    if a[-1] == b[-1]:
        if len(a) == len(b):
                print("=")
        if a[-1] == "S" and b[-1] == "S":
            if a.count('X') < b.count('X'):
                print(">")
            else:
                print("<")
        if a[-1] == "L" and b[-1] == "L":
            if a.count('X') < b.count('X'):
                print("<")
            else:
                print(">")
    if a[-1] != b[-1]:
        if a[-1] == "M" and b[-1] == "S":
            print(">")
        else:
            print("<")
        if (a[-1] == "L" and b[-1] == "M") or (a[-1] == "L" and b[-1] == "S"):
            print(">")
        else:
            print("<")

test_case = int(input())
for _ in range(test_case):
    a, b = input().split()

print(Tsize(a, b))

