# LECAVELIER Maeva - POUEYTO Clement G2

from turtle import*
from math import*
from plateau import*
import random

x_epee=0
y_epee=0
longueurBase=20*0.3
up()
goto(0,0)
down()

################ permet de connaître la position finale du curseur, pour redessiner les autres dessins par rapport à la position ########
    
def maj(): #ça return donc une liste de la forme [x,y]
    return position()

##########################

########je return x et y séparément ######

def returnX():
    return maj()[0]

####################################################


########## y : #####################################

def returnY():
    return maj()[1]

####################################################

def carre(longueurBase,plein,x_epee,y_epee): #trace un carré. Le paramètre plein permet de savoir si on fait fill ou pas. Les contours rendent le dessin plus propre 
    up()
    goto(x_epee,y_epee)
    down()
    if plein == 1 :
        begin_fill()
    j=0
    while j<4: #vu en cours
       forward(longueurBase)
       left(90)
       j=j+1
    forward(longueurBase)
    if plein == 1:
        end_fill()
#####################################################

###### 
def epeePleine(x_epee,y_epee,longueurBase): #dessine une épée avec les couleurs
    l=longueurBase
    left(45)
    up()
    goto(x_epee,y_epee)
    down()
    begin_fill()
    for i in range(18):#ça dessine les épées comme une ligne verticale de carrés. Pour ceux sur les côtés, c'est la fonction "garde"
        if i == 0:#pommeau de l'épée, d'une couleur aléatoire issue des différentes factions de la série Game of Thrones
            couleurListe=[[1,0,0], [1,0.83,0], [1,1,1], [0,0,0], [0.7,0.7,0.7], [0,1,0], [1,0.64,0]]
            couleur=couleurListe[random.randint(0,len(couleurListe)-1)]
            color(couleur[0],couleur[1],couleur[2])
            carre(l/2,1,x_epee,y_epee)
        elif i == 1: #début du manche de l'épée
            color(0.60,0.32,0.17)#marron
            carre(l*1.5,1,x_epee,y_epee+i*sqrt(longueurBase*longueurBase)/1.5)
            color(0.50,0.267,0.142)
            carre(l*1.5,0,x_epee,y_epee+i*sqrt(longueurBase*longueurBase)/1.5)
        elif i == 2 or i == 3 : #manche de lépée
            color(0.67,0.31,0.03) #marron plus clair
            carre(l,1,x_epee,y_epee+(i+1)*sqrt(longueurBase*longueurBase)/1.5)
            color(0.55,0.254,0.025)
            carre(l,0,x_epee,y_epee+(i+1)*sqrt(longueurBase*longueurBase)/1.5)
        elif i == 4 or i == 5 :#début de la garde
            color(1,0.83,0) #gold
            carre(l,1,x_epee,y_epee+(i+1)*sqrt(longueurBase*longueurBase)/1.5)
            color(0.8,0.664,0)
            if i == 4 :#dessine la garde
                y_epeeGarde=returnY()
            color(1,0.83,0)
            garde(i,1,x_epee,y_epeeGarde,longueurBase)
        else :#dessine la lame
            color(0.7,0.7,0.7)
            carre(l,1,x_epee,y_epee+(i+1)*sqrt(longueurBase*longueurBase)/1.5)
            color(0.6,0.6,0.6)
            carre(l,0,x_epee,y_epee+(i+1)*sqrt(longueurBase*longueurBase)/1.5)
       
    right(45)#rétablit la turtle pour les dessins suivants
    end_fill()

############# garde de l'épée ##################
        
def garde(i,plein,x_epee,y_epeeGarde,longueurBase=longueurBase):
    y_epeeGarde=y_epeeGarde-sqrt(longueurBase*longueurBase)/4
    x_epee=x_epee
    if plein == 1 :
        begin_fill()
    if i == 4 :
        orientation = -1 #on dessine la partie gauche du manche
        
    else :
        orientation = 1 # on dessine la partie droite
        
    for j in range(3):
        x_epee=x_epee+(orientation*3*sqrt(longueurBase*longueurBase))/4
        carre(longueurBase,1,x_epee,y_epeeGarde)
    if plein == 1 :
        end_fill()

###############################################

#On affiche les epees

######## dessine le bon nombre d'épées #######################
#fonction qui s'occupe de la disposition des épées en fonction de leur nombre
        
def repeteEpee(distance,nbAllum,x_epee,y_epeeRep,multip4,longueurBase,restant,cpt_epee):
    if cpt_epee == -1 :
        retablir=-1
    else :
        retablir=0
    while cpt_epee<(multip4+restant)+retablir: #c'est pour adapter le dessin selon le nombre d'épées : "retablir" rétablit le dessin. Soit on part de multip4+restant -1 soit de multip4+restant
        if cpt_epee%2 == 1 : #on gère l'alternance
            y_epeeRep=y_epeeRep+20
        else :
            y_epeeRep=y_epeeRep-20
        x_epee=x_epee+distance
        epeePleine(x_epee,y_epeeRep,longueurBase)
        cpt_epee=cpt_epee+1
        
##############################################################
        
#### affiche le message sur le panneau #######################

def afficheMessage(haut,ordiRetire,nbAllum,regle):
    color("black")
    up()
    goto(0,haut/4)
    down()
    if ordiRetire!=0: #si c'est au tour de l'ordinateur, on affiche son action
        write(("L'ordinateur a retiré "+str(ordiRetire)+" allumette(s)"),False,align="center",font=("Herculanum", 29, "normal"))
    up()
    goto(0,haut/6)
    down() #ecrit le nombre d'épées restantes
    write(("Il reste "+str(nbAllum)+" allumette(s). Règle: "+str(regle)),False,align="center",font=("Herculanum", 27, "normal"))

################# Adapate la taille des épees ###################
    
def facteur_taille(nbAllum): #change la taille des épées selon le nombre d'allumettes restantes
    if nbAllum<=5:
        fact_epee=0.4
    elif nbAllum>5 and nbAllum<=20:
        fact_epee=0.3
    else:
        fact_epee=0.25
    longueurBase=20*fact_epee
    return longueurBase #renvoie la taille des épées

#################################################################

def facteur_distance(nbAllum):
    if nbAllum<=5:
        fact_distance=50
    elif nbAllum>5 and nbAllum<=20:
        fact_distance=30
    else:
        fact_distance=0
    return fact_distance

############## Dessine l'ensemble des épées en fonction du nombre restant ###############################

def dessineEpee(x_epee,y_epee,nbAllum,long,haut,ordiRetire,regle):
    cpt=0 # compteur
    plateau(long,haut)# on dessine le plateau
    longueurBase=facteur_taille(nbAllum)
    fact_distance=facteur_distance(nbAllum)
    afficheMessage(haut,ordiRetire,nbAllum,regle) #on écrit les informations
    multip4=nbAllum//4 # variable qui permet de savoir le multiple de 4 du nombre d'épées. C'est pour faciliter le dessin
    while cpt<2:
        restant=0
        if cpt==0:
            y_epee=0 #première ligne d'épées
            restant=nbAllum%4 #savoir combien d'épées il reste en plus par rapport au mutliple de 4
        else:
            y_epee=-haut/6-20  #deuxième ligne d'épées          
        distance=25+fact_distance #distance entre les épées (partie droite)
        x_epee=-distance
        if restant%2 == 1 :
            adaptation = 1 #c'est les épées qui sont en plus, pour ne pas oublier de les dessiner (il rest donc épée)
        else :
            adaptation = 0
        repeteEpee(distance,nbAllum,x_epee,y_epee,multip4,longueurBase,restant//2 + adaptation,0)#on dessine les allumette de la partie droite de la ligne 
        x_epee=0
        y_epee=y_epee-15 
        distance=-25-fact_distance #distance entre les épées (partie gauche)
        repeteEpee(distance,nbAllum,x_epee,y_epee,multip4,longueurBase,restant//2,-1)#puis celles de la partie gauche de la ligne. Ainsi, c'est presque symétrique (à cause de l'adaptation ça ne l'est pas forcément)
        cpt=cpt+1

###################################################################



    
