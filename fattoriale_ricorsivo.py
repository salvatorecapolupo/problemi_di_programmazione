import random

def fattoriale(n):
    if (n==0 or n==1):
        return 1
    else:
        return fattoriale (n-1) * n

c = random.randint(0,100);
print ( "numero = ",c )
print ( "fattoriale = ",fattoriale(c) )
