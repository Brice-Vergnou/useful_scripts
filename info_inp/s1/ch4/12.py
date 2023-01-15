def f(liste1 ,liste2 ):
    liste1.extend(liste2)
    liste1 [ -1][0]=9
    return liste1
#------------------------
def g(liste1 ,liste2 ):
    liste1=liste1+liste2
    liste1 [ -1][0]=9
    return liste1
#------------------------
def h(liste1 ,liste2 ):
    liste2=liste2 +[[9 ,9]]
    liste1=liste1+liste2
    liste1 [ -1][0]=0
    return liste1
#------------------------

L=[[1 ,2] ,[3 ,4]]
M=[[5 ,6] ,[7 ,8]]
print(f(L,M)) # effet de bord, les sous listes ajoutées ont le meme id qu'avant
print(M)
L=[[1 ,2] ,[3 ,4]]
M=[[5 ,6] ,[7 ,8]]
print(g(L,M)) # meme chose
print(M)
L=[[1 ,2] ,[3 ,4]]
M=[[5 ,6] ,[7 ,8]] # la derniere sous liste n'est pas assigné à une variable, elle ne peut donc avoir un id partagé
print(h(L,M))
print(M)


[['2', '6', '3', '6', '3'],
 ['4', '1', '5', '4', '2'],
 ['5', '4', '2', '4', '1'],
 ['6', '1', '5', '2', '3'], 
 ['4', '1', '5', '1', '2'], 
 ['5', '4', '2', '4', '1']]