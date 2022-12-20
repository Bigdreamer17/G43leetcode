# Enter your code here. Read input from STDIN. Print output to STDOUT
# Intianlizing our happiness
happiness = 0
# accept inputs n and m
len_list, len_set = input().split()
# creating our list of numbers
list_num = [int(i) for i in input().split(" ", int(len_list)-1)]
# creating our two disjoint sets
set_A = set(int(i) for i in input().split(" ", int(len_set)-1))

set_B = set(int(i) for i in input().split(" ", int(len_set)-1))

# checking if our list values are in A or B
for i in list_num:
    if i in set_A:
        happiness += 1
    elif i in set_B:
        happiness -= 1
print(happiness) 