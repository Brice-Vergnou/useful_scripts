A=3
B=12
chaine1 = str(A)+" fois 4 = "+str(B)
chaine2 = str(B+1)+" = "+str((B+1)//A)+" x "+str(A)+" + "+str((B+1)%A)
print(chaine1)
print(chaine2)
ch1= "{} fois 4 = {}".format(A,B)
ch2 = "{} = {} x {} + {}".format(B+1,(B+1)//A,A,(B+1)%A)
print(ch1)
print(ch2)
ch1= f"{A} fois 4 = {B}"
ch2 = f"{B+1} = {(B+1)//A} x {A} + {(B+1)%A}"
print(ch1)
print(ch2)