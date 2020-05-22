# LECAVELIER Maeva - POUEYTO Clement G2
#plateau de jeu
from turtle import *

setup(width=1.0, height=1.0)
long=window_width() # je récupère la taille de la fenêtre 
haut=window_height()
print(long,haut)

### pour le coin du plateau ########
def escalier():
    for k in range(20):
        forward(2)
        left(90)
        forward(2)
        right(90)

###################################

### pour les pieds du plateau #####
        
def rectangle(longueurPied,cote, haut=haut,long=long): #cote permet de savoir de quel côté on dessine le rectangle (une fois negatif : a gauche, et la deuxième fois positif : a droite)
    begin_fill()
    xDebutPied = cote*long/6
    if cote == 1:
        xDebutPied = xDebutPied-longueurPied
    up()
    goto(xDebutPied,-1/4*haut)
    down()
    right(90)
    for cpt in range(2):
        forward(haut/2)
        left(90)
        forward(longueurPied)
        left(90)
    end_fill()
    up()
    home()     
##################################

### le plateau ###################
    
def plateau(long,haut):
    begin_fill()
    up()
    goto(-1/4*long,-1/4*haut)
    down()
    color(0.586,0.39,0.11)
    for cpt in range(2):
        forward(long/2)
        escalier()
        left(90)       
        forward(haut/2)
        escalier()
        left(90)
    goto(-1/4*long,-1/4*haut)
    end_fill()
    rectangle(50,-1)
    rectangle(50,1)
    up()
    home()

###############################
