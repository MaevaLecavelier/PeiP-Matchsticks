# LECAVELIER Maeva - POUEYTO Clement G2


###branche###
from turtle import*
import random
from epee import*
from dragon import*
import os

######## déclaration des variables : ####
x=0  # coordonnées classiques
y=0
up()
goto(x,y) 
down()
color('black')
tracer(0)
setup(width=1.0, height=1.0)#mettre en plein écran 
l=40 #c'est la hauteur de l'arbre de base
longueur = window_width() # je récupère la taille de la fenêtre (pour le sol et le ciel)
hauteur = window_height()

######## dessine un rectangle dont la largeur est deux fois plus grande que la hauteur. (utilisée pour les branches et le sol) #######

def rectangle(x=0, y=0, orientation=0,f=1, l=10): # orientation permet de savoir si le rectangle est en portrait ou en paysage. 1 = paysage, 0 = portrait 
    i = 0
    up()
    goto(x,y)
    down()
    begin_fill()
    while i < 4:
        if orientation%2 == 1 :
            forward((2*l)*f) #f c'est le facteur de grossissement. Par défaut à 1. Ici on dessine le grand côté.
            left(90)
        else:
            forward(l*f)# dessin du petit côté
            left(90)
        i = i+1
        orientation = orientation+1 # on incrémente l'orientation pour dessiner ceux de l'autre sens
    end_fill()
    maj()
    
######################################################

################ permet de connaître la position finale du curseur, pour redessiner les autres dessins par rapport à la position ########
    
def maj(): #ça return donc une liste de la forme [x,y]
    return position()

##########################


######## return x et y séparément pour manier plus facilement les coordonnées ######

def returnX():
    return maj()[0]

####################################################


########## y : #####################################

def returnY():
    return maj()[1]

####################################################


#######le motif des branches/feuilles dans les arbres, inspiré d'une image google

def branche(x,y,f=1):
    begin_fill()
    couleur = random.uniform(0.05,0.5)
    color(couleur*1.2, couleur*1.8, couleur*1.7)#couleur aléatoire orientée vert
    # cette mutlitude d'appel de fonction permet de dessiner chaque rectangle individuellement
    rectangle(x,y,0,f) # première branche
    rectangle(x+10*f,y+20*f,1,f)
    rectangle(x+30*f,y+30*f,0,f)
    rectangle(x+30*f,y+10*f, 1,f)
    rectangle(x+50*f,y-10*f,0,f)
    rectangle(x+20*f,y+50*f,0,f)
    rectangle(x+30*f,y+70*f,0,f)
    rectangle(x+0,y+40*f,1,f)
    rectangle(x-10*f,y+50*f,0,f)
    rectangle(x-30*f,y+70*f,1,f)
    rectangle(x-20*f,y+20*f,1,f)
    rectangle(x-30*f,y+30*f,0,f)
    rectangle(x-50*f,y+50*f,1,f)
    rectangle(x-70*f,y+10*f,0,f)
    rectangle(x-60*f,y+30*f,0,f)
    end_fill()

###########################################################


############# arbre : #####################################
    
def arbre(x,y,l,f=1):
    i=0
    up()
    goto(x,y)
    down()
    begin_fill()
    l=40
    #on dessine le tronc (on appelle pas rectangle car elle est faite pour les rectangles de dimension x sur 2x)
    while i < 4:
        if i%2 == 1 :
            forward((2*l)*f)
            left(90)
        else:
            forward(10*f)
            left(90)
            if i==2:
                x=returnX() #utile pour l'appel de la fonction branche. On part du coin supérieur gauche de l'arbre pour dessiner les feuilles 
                y=returnY() # du coup on return x et y quand c'est dans ce coin là
        i = i+1
    end_fill()
    x=x+10*f #pour que ça se place bien au bon endroit en gros
    branche(x,y,f)# et on appelle branche pour faire les branches de  l'arbre, avec le même facteur de grossissement f et les coord x et y

#############################################


################ foret : appelle arbre qui appelle branche qui appelle rectangle ##############################
def foret(x=-150,y=-275,l=10,f=0.05,hauteur=hauteur):
    while x > -1000 and y >(-6.5*hauteur+hauteur)/7.5 and f < 28: #limiter le grossissement pour éviter que ça devienne trop gros
        #petits arbres dans le fond
        while x > -250 and f < 15: #dessine les petits arbres jusqu'à un certain point ou une certaine taille
            couleur = random.uniform(0.05,0.5)
            color(couleur*1.9, couleur*1.5, couleur*1.8)#couleur aléatoire orienté marron pour dessiner le tronc
            arbre(x,y,l,f)
            up()
            goto(x-3,y-1)#je me déplace un peu sur la gauche
            f=f*1.08 #le prochain arbre est plus gros
            x = returnX() #pour mettre a jour la nouvelle position
            y = returnY()
        #moyens arbres (l'écartement devait être différent car sinon ça faisait trop serré
        while x > -300 and f < 20:
            couleur = random.uniform(0.05,0.5)
            color(couleur*1.9, couleur*1.5, couleur*1.8)
            arbre(x,y,l,f)
            up()
            goto(x-12,y-1)
            f=f*1.3
            x = returnX()
            y = returnY()
        # un peu plus gros
        couleur = random.uniform(0.05,0.5)
        color(couleur*1.9, couleur*1.5, couleur*1.8)
        arbre(x,y,l,f)
        up()
        goto(x-45,y-1)
        f=f*1.20
        x = returnX()
        y = returnY()
        
####################################################


###############le sol couleur neige ################

def sol(): # on  dessine un grand rectangle dans le bas du background
    up()
    goto(-longueur/2,-hauteur/2)
    down()
    color(0.80,0.90,0.95)
    i=0
    begin_fill()
    while i < 4:
        if i%2 == 0 :
            forward(longueur)
            left(90)
        else:
            forward(hauteur/7.5)
            left(90)
        i=i+1
    end_fill()

########################################################################


########### le ciel couleur bleu pâle ##################################
    
def ciel(): #on dessine un grand rectangle dans le haut du background
    up()
    goto(-longueur/2, -hauteur/2)
    down()
    color(0.65,0.90,1)
    begin_fill()
    i=0
    while i <4:
        if i%2 == 0:
            forward(longueur*2)
            left(90)
        else :
            forward(hauteur*2)
            left(90)
        i = i+1
    end_fill()

######################################################################


######### wall #############

def wall(longueur=longueur, hauteur=hauteur):
    up()
    home()
    color(0.49,0.64,0.76)
    goto(90, ((-hauteur/2)+hauteur/6.5))
    down()
    begin_fill()
    i=0
    while i<80: # dessine un escalier pas droit pour faire comme si cétait irrégulier
        left(55)
        forward(i/2)
        right(55)
        forward(i/3)
        i=i+1
    goto(longueur/2, -hauteur/2) # on rejoint les autres points du mur pour finir le dessin
    goto(90, ((-hauteur/2)+hauteur/7.5))
    up()
    end_fill()

##############################

##############################

def porte(longueur=longueur, hauteur=hauteur): #pas adapté à tous les écrans
    up()
    color(0.29,0.44,0.56)
    begin_fill()
    goto(longueur/2.1, -hauteur/2)
    left(90)
    forward(hauteur/8)
    i=0
    while i<50:
        left(3)
        forward(2+(i/12)) #i = facteur grossissant pour la perspective
        i=i+1
    left(27)
    forward(hauteur/13)
    goto(longueur/2.1, -hauteur/2)
    end_fill()
    left(93)
    
######################################

######################################
def porteOmbre(longueur=longueur, hauteur=hauteur): #pas adapté à tous les écrans
    color(0.18,0.20,0.22)
    begin_fill()
    goto(longueur/2.1, -hauteur/2)
    left(90)
    forward(hauteur/8)
    i=0
    while i<50:
        left(3)
        forward(2+(i/20))#i = facteur grossissant pour la perspective
        i=i+1
    left(28)
    forward(hauteur/10.5)
    goto(longueur/2.1, -hauteur/2)
    end_fill()
    home()
    up()

###########################
def paysage(): # appelle tout le décor fixe, fonction par fonction avec un ordre précis pour que les éléments se superposent bien
    ciel()
    sol()
    foret(-200)
    foret()
    wall()
    porte()
    porteOmbre()
    dragon(longueur/5, hauteur/2.5,0.55)
    dragon(longueur/2.5 - 30, hauteur/2.5 - 10, 0.7)
    dragon(longueur/4, hauteur/2.7, 1)
    up()

