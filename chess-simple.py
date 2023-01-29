# stampa una scacchiera 8x8 
white = " "
black = "■"

w, h = 8, 8
scacchiera = [ [0 for x in range(w)] for y in range(h) ]

for i in range (0, w):
  for j in range (0, h):
    if (i+j)%2 == 0:
      scacchiera[i][j] = white
    else:
      scacchiera[i][j] = black
      
for i in range (0, w):
  riga = ""
  for j in range (0, h):
    riga = riga + scacchiera[i][j]
  print (riga)
  
  ############ output ########
  
 ■ ■ ■ ■
■ ■ ■ ■ 
 ■ ■ ■ ■
■ ■ ■ ■ 
 ■ ■ ■ ■
■ ■ ■ ■ 
 ■ ■ ■ ■
■ ■ ■ ■ 
