import turtle as tl
 
 
def courbeVonKoch(  n, cote  ) :
    if n == 0 :
        tl.forward(cote)
    else :
        courbeVonKoch(n-1, cote/3)
        tl.left(60)
        courbeVonKoch(n-1, cote/3)
        tl.left(-120)
        courbeVonKoch(n-1, cote/3)
        tl.left(60)
        courbeVonKoch(n-1, cote/3)
 
 
def flocon(n, cote) :
    for _ in range(3) :
        courbeVonKoch(  n, cote  )
        tl.left(-120)
 
screen = tl.Screen()
tl.setheading(0) # orientation intiale de la tête : vers la droite de l'écran
tl.hideturtle() # on cache la tortue
tl.speed(0)  # on accélère la tortue
tl.color('green')
flocon(  n = 3, cote = 200  )
tl.exitonclick() # pour  garder ouverte la fenêtre