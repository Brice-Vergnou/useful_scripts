def triangle(n):
    liste = [[1]]
    for i in range(n+1):
        previous = liste[i]
        next = [1] + [previous[j]+previous[j+1] for j in range(len(previous)-1)] + [1]
        liste += [next]
    return liste
    
print(triangle(5))


