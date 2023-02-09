#somma di tutti i numeri da 1 a 100
somma = 0
cento = 101
for numero in range(1,cento):
  somma = somma + numero 
print()
print ("la somma dei primi 100 numeri è: ", somma)

print()
print ("Come ha fatto Gauss? ")

numerocoppie = 0
for i in range(1, cento): 
  primo  = i 
  ultimo = cento-i
  numerocoppie = numerocoppie + 1 
  
  if i >= 1 and i<= 6:
    print(primo," + ",ultimo, " = ",primo + ultimo)
  elif i==7:
    print ("...")

print( " numero coppie: ", numerocoppie )
print( " moltiplicando: ",cento," * ",numerocoppie ) 
print (" e dividendo per 2, otteniamo: ",int(cento*numerocoppie/2) )

print (" morale: ci sono più modi per risolvere lo stesso problema :-) ")
