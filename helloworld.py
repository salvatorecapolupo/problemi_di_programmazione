import datetime

print ("Bella, mondo!")
x = datetime.datetime.now()

giorno  = str(x.day) + "-"+ str(x.month) + "-"+ str(x.year)
ore     = str(x.hour) +":"+ str(x.minute)

print ("Oggi è il: ", giorno, " e sono le: ", ore)
