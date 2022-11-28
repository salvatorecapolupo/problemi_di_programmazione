import cmath 

print ("equazioni di secondo grado nella forma: ")
print("ax**2 + b*x + c = 0")
#a, b, c reali
#a ≠ 0

a=0
while (a == 0):
  a = float( input(" a= ") )
  b = float( input(" b= ") )
  c = float( input(" c= ") )
  if ( a==0 ):
    print ("a deve essere > 0")
  
print ("risolviamo l'equazione:")

# discriminante
d = (b**2) - (4*a*c)

r1 = ( -b-cmath.sqrt(d) )/( 2*a )
r2 = ( -b+cmath.sqrt(d) )/( 2*a )

print('Le soluzioni sono {0} e {1}'.format(r1,r2))
