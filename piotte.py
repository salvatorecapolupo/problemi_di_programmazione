#convertitore euro in piotte / sacchi / testoni
import random 

for i in range(1,4):
  euro   = random.randint(5,50000)

  scudi   = round( euro / 5, 2 )    # 1 scudo  = 5 €
  piotte  = round( euro / 100 )     # 1 piotta = 100 €
  testoni = round( euro / 1000, 2 ) # 1 testone  = 1000 €

  print (euro, " € corrispondono a: ")
  print (scudi, " scudi ")
  print (piotte, " piotte ")
  print (testoni, " testoni ")
  print () 
