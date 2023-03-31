test_case = int(input())
for _ in range(test_case):
    num = int(input())
    if num == 1:
        print(3)
    else:
        And = ((num - 1) & num) ^ num
        ans = num ^ And
        if ans != 0:
            print(And)
        else:
            print(And + 1)

