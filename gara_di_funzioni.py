def fibo(N):
    if N==1 or N==2: 
        return 1
    else: 
        return fibo(N-1) + fibo(N-2)
        
def fatt(N):
    if N==0:
        return 1
    else: 
        return N * fatt(N-1)   

def espo( a,b ):
    res = 1
    for j in range(1, b):
        res = res * a
        
    return res
    
def bar(n):
    res=""
    for i in range (1,n):
        res = res + "▓"
        
    return res
    
for n in range(1, 10):
    print ("passo ",n)
    print ( "fatt: ", bar ( fatt(n) ) )
    print ( "fibo: ", bar ( fibo(n) ) )
    print ( "espo: ", bar ( espo(2,n) ) )
    print ()
