n = int(input())
dic = {}
for _ in range(n):
    wor =input()
    word = wor.split()
    for i in range(len(word)):
        for j in range(len(word[i])):
            if word[i][j].isdigit():
                dic[int(word[i][j])] = word[i].replace(word[i][j],'',1)
od = sorted(dic.items(), key=lambda x: (x[0]))
ans = [value for key, value in od]
print(' '.join(ans))
"""worl2d hell1o
i2s th1s a3 t4est"""