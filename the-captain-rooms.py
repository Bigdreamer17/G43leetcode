# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room_num = input().split()

freq = {}
for item in room_num:
    if int(item) in freq:
        freq[int(item)] += 1
    else:
        freq[int(item)] = 1
for key, value in freq.items():    
    if value == 1:
        print(key)