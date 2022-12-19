def split_and_join(line):
    # write your code here
    ans = line.split(" ")
    return '-'.join(ans)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)