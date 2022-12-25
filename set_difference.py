# Enter your code here. Read input from STDIN. Print output to STDOUT
english_number = int(input()) 
english_paper = set(map(int , input().split()))

french_number = int(input()) 
french_paper = set(map(int , input().split()))

print(len(english_paper.difference(french_paper)))