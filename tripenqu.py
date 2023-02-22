import random
n = random.randint(1,5)

t = 0
for i in range (1, n+1):
    t = t + i

q = 0
for i in range (1, n+1):
    q = q + 2*i-1

p = 0
for i in range (1, n+1):
    p = p + 3*i-2
    
print (" n=",n)
print (" --- " )
print (" t=",t)
print (" q=",q)
print (" p=",p)