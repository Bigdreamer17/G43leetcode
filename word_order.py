from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_words = int(input())
word = []
for _ in range(num_words):
    words = str(input())
    word.append(words)
a = dict(Counter(word))
b = list(a.values())
rep = ' '.join(str(i) for i in b)
print(len(b))
print(rep)