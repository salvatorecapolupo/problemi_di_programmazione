import random

# generare numeri float casuali
v = []
for i in range(1,10):
  random_number = random.random()
  v.append(random_number)
print(v)

# generare numeri interi casuali
j=0
for x in v:
  v[ j ] = round( x * 100 )
  j=j+1

print(v)

#[0.6781544428268317, 0.28316169796503987, 0.07690959490640059, 0.43845572173873293, 0.6278164622487402, 0.409925656053862, 0.6925556023977163, 0.17176666761564052, 0.04210667670536594]
#[68, 28, 8, 44, 63, 41, 69, 17, 4]
