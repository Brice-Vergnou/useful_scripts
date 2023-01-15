def triangle1(c,n):
    for i in range(n):
        print(c*(n-i))
        
triangle1("#",4)

def triangle2(c,n):
    for i in range(1,n+1):
        print(" "*(n-i)+i*c)

triangle2("*",6)

def triangle3(c,n):
    for i in range(1,n+1):
        print(i*c)
    for i in range(1,n):
        print(c*(n-i))
        
triangle3("*",4)

def triangle4(c,n):
    for i in range(1,n+1):
        print(" "*(n-i)+c*(2*(i-1)+1))
              
triangle4("+",5)