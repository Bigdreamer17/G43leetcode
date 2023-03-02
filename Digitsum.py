def superDigit(n, k):
    # Write your code here
    # Base case
    if len(n) == 1 and k == 1:
        return int(n)
    else:
        summ = sum(list(map(int, n)))
        return superDigit(str(summ * k), 1) 
