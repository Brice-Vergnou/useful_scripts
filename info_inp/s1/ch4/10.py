n = 1
while str(n)[::-1] != str(n*9):
    n+=1

print(n, n*9)