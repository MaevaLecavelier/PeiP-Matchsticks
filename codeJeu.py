# LECAVELIER Maeva - POUEYTO Clement G2


#Projet Version ++++ 1.6
import random
from turtle import *
from IA import *
nbAllum=0
ordiRetire=0
endgame=0
n=random.randint(1,2)


###########################################################################
#TIRE LES REGLES ALEATOIRES
############################################################################

def regleAleatoire(mdj): #hasard pour les règles il peut y avoir 3 4 5 6 7 ou 8
    if mdj==2: #si le mode de jeu est 2 = "aléatoire"
        regle1=[1,2]
        autreValeur=1 #pour dire qu'on rajoute une valeur dans la liste
        while autreValeur==1:
            R1=random.randint(3,8) # valeur de la liste allant de 3 à 8
            i=0
            while i<len(regle1): #filtre si la valeur est deja dans la liste
                if R1==regle1[i]:
                    regle1.remove(R1)
                i=i+1
                k=0
            while k<len(regle1) and R1>regle1[k]: #esthetique: place dans l'ordre croissant
                k=k+1
            regle1.insert(k,R1)
            autreValeur=random.randint(0,1) # 1 chance sur 2 de rajouter une valeur dans la liste
            i=i+1
    else: #si le mode de jeu est 1 = "classique"
        regle1=[1,2,3]
    return regle1

    
#############################################################################
#fonction : le joueur retire des allumettes
#############################################################################

def retireAllum(nbAllum,regle,mdj):
    choix=0
    condition=False
    if mdj==2: #pour le mode de jeu aléatoire
        while condition==False: #tant que la condition n'est pas remplie : c'est-à-dire que le joueur n'a pas donné une valeur valable
            c=0
            choix=int(numinput("A votre tour !","Combien d'allumette(s) à retirer ? ",1,1,8))
            while c<len(regle):
                if choix==regle[c] and nbAllum>=choix: # on vérifie les conditions de validité
                    condition=True
                c=c+1
    else: #pour le mode de jeu classique
        while choix<1 or choix>3: #assure de prendre le bon nombre d'allumettes
            choix=100 # pour être sur qu'on rentre dans la boucle la première fois
            while choix>nbAllum: #assure de ne pas retirer plus d'allumettes que ce qu'il y en a.
                choix=int(numinput("A votre tour !","Combien d'allumette(s) à retirer ? (1, 2 ou 3) : ",1,1,3))
                condition=True
    nbAllum=nbAllum-choix
    return nbAllum


#############################################################################
#fonction : le jeu peut continuer ?
############################################################################

def jeuValide(nbAllum):
    if nbAllum > 0: #tant qu'il reste des allumettes
        endgame=0 #le jeu continue
    else: #sinon la partie est finie
        nbAllum=0
        endgame=1
    return endgame #vérifie que la partie peut continuer et qu'elle n'est pas terminée


#############################################################################
#fonction: l'ordinateur retire X allumettes
############################################################################

def playOrdinateur(nbAllum, ordiRetire):
    nbAllum=nbAllum-ordiRetire
    return nbAllum #renvoie le nombre d'allumettes apres le tour de l'ordinateur



###############################################################################
# IA EN MODE FACILE ##
############################################################################

def ordinateurFacile(regleOrdi,nbAllum,mdj):
    ordiRetire=1000 #on veut juste un nombre au dessus de 40 : pour rentrer dans la boucle
    if mdj==2: # mdj 2 difficulte facile
 
        while ordiRetire>nbAllum: #ne pas retirer plus que ce qu'il y a d'allumettes.
            ordiRetire=0
            limite=len(regleOrdi)-1
            r=random.randint(0,limite)#indice de la liste "regle" 
            ordiRetire=regleOrdi[r] #prend un chiffre dans "regle"
    else: # mdj 1 difficulte facile
        while ordiRetire>nbAllum:
            ordiRetire=random.randint(1,3)

    return ordiRetire



#############################################################################
# TIRE ALEATOIREMENT LE NOMBRE D'ALLUMETTES #
############################################################################

def modeDeJeu(mdj,nbAllum):
    if mdj==2:
        nbAllum=random.randint(15,40) # entre 15 et 40 allumettes pour le mode de jeu aléatoire
    else:
        nbAllum=random.randint(15,20) #entre 15 et 20 allumettes pour le mode de jeu classique
    return nbAllum


###########################################################################


