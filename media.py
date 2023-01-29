def calcola_media(v,n):
    media = 0 # inizializza a valore numerico "neutro", ancora non l'ho calcolata
    for elemento in v:
      media = media + elemento
      
    return round (media/n,2)
    
v = [] # array vuoto 
v.append(1.95) # altezza 1 studente
v.append(1.92) # altezza 2 studente
v.append(1.85) # altezza 3 studente
v.append(1.78) # altezza 4 studente

print (v)

print ( "media altezze: ", calcola_media(v, len(v)) )
    
    
