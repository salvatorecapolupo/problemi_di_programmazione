import random
i=80

chars = ['+', '-']

while (i>0):
  r  = random.choice(chars)
  print(r, end='')
  
  i = i-1
