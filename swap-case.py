def swap_case(s):
    str_ = []
    for i in s:
        if i.isalpha() and i.islower():
            str_.append(i.upper())
        elif i.isalpha() and i.isupper():
            str_.append(i.lower())
        else:
            str_.append(i)
    return ''.join(str_)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)