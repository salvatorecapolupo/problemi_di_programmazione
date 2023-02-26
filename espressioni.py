# esercizio 1 
x = 2          # a statement
x = x + 2      # an expression
print (x)

# esercizio 2
x = "2"          # a statement
x = x + "2"      # an expression
print (x)

# esercizio 3
x = 1.5          # a statement
x = x - 2.5      # an expression
print (x)

# esercizio 4
x = 1            # a statement
x = x - 2.5      # an expression
print (x)

# esercizio 5
x = 10          
x = x / 3      
print (x)

# esercizio 6
x = 10          
x = x // 3      
print (x)

# esercizio 7
x = 10          
x = x ** 2      
print (x)

# esercizio 8
x = 10          
x = x % 2      
print (x)

# esercizio 9
x = 10          
x = x * 2      
print (x)

# esercizio 10
x = 10          
x = x ** 2      
print (x)

# esercizio 11
a = True          
b = False
c = True
print ( not a )
print ( a and b)
print ( a or b)
print ( a and b or c)

# esercizio 12
a = 1          
b = 2
c = 3 
print ( a + b - c * a // b)

# esercizio 13
a = 1          
b = 2
c = 3 
print ( a // b - c * a - b)

# esercizio 14
a = 1          
b = 2
c = 3 
print ( a ** b ** c)

# esercizio 15
a = 1          
b = 1
print ( a <= b )

# esercizio 16 
a = 1.1 + 2.2      
valore_atteso = 3.3
print ( a == valore_atteso ) # attenzione

# esercizio 17
a = 1.1 + 2.2   
valore_atteso = 3.3
tol = 0.00001
print ( abs(a - valore_atteso) < tol ) # attenzione ...pure qui 

# esercizio 18 
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

sum = int(num1) + int(num2)
sub = int(num1) - int(num2)  
mul = float(num1) * float(num2)  
div = float(num1) / float(num2) 

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The subtration of {0} and {1} is {2}'.format(num1, num2, sub))
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))

# esercizio 19: pari o dispari
num1 = input("Enter a number: ") 
if (int(num1) % 2) == 0:  
   print("{0} is Even number".format(num1))  
else:  
   print("{0} is Odd number".format(num1)) 
    
#esercizio 20 - numeri primi
def PrimeChecking(num):  
    if num > 1:  
        for i in range(2, int(num/2) + 1):  
            if (num % i) == 0:  
                print("The number ",num, "is not a prime number")  
                break  
        else:  
            print("The number ",num, "is a prime number")  
    else:  
        print("The number ",num, "is not a prime number")  
num = int(input("Enter a number to check prime or not: "))  

PrimeChecking(num)
