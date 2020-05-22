# LECAVELIER Maeva - POUEYTO Clement G2

import random

####################### DEF POUR IA ###################################

#Les variables avec seulement une lettre ne sont que des variables "compteur"(incrémentation)

################### verifie si l'IA peut gagner #########################

def checkVictory(regleOrdi,ordiRetire,nbAllum,taille):
    q=0
    while q<taille:          #l'ordi vérifie s'il peut gagner sur ce tour
        if regleOrdi[q]==nbAllum: #pour chaque valeur de règle
            ordiRetire=nbAllum
            return ordiRetire #si oui on retourne la valeur
        q=q+1
    return 0 #sinon on retourne la valeur 0. Et tant que ordiRetire==0 on continue dans le programme
    
#############################################################################
################ trie les mauvaises valeurs #################################

def Anticipation(regleOrdi,nbAllum,got,taille):
    e=0 #rang du coup de l'ordi (il se déplace dans la liste pour tester chaque valeur qu'il va jouer
    while e<taille: #cette première boucle sert à tester les valeurs de la règle (taille = len(regleOrdi)
        f=0 #rang du coup du joueur, on se déplace pour tester toutes les possibilités
        while f<taille:
            anticipation=nbAllum-regleOrdi[e]-regleOrdi[f] #calcul son coup plus celui de l'adversaire (on parcourt la liste 2 fois)
            #Si ça vaut 0, c'est que la valeur qu'il a prise, mène à la victoire du joueur
            if anticipation!=0: #on cherche à ce que le calcul soit différent de 0 sinon il perd
                f=f+1                
            else: #si une des valeurs de la regle fait perdre l'ordi alors on la range dans la liste "got"
                got.append(regleOrdi[e])
                f=f+1
        e=e+1
    return got

#############################################################################
############ Determine le plan de jeu de l'ordinateur #################################

def regleModulo(suite,regle): # on part du rang 2 car il y a toujours au moins 2 rangs dans nos règles
    while suite<len(regle) and regle[suite]==(suite+1): #verifie si il y a une suite de nombre pour pouvoir appliquer la regle du modulo
            suite=suite+1                               #ex [1,2,3,4,5] applique la regle du modulo 6
    return suite

#############################################################################
################ Applique le plan de jeu ####################

def ModuloPlus(regle,nbAllum,ordiRetire,got,suite):
    if suite>2:
        cheat=nbAllum%(suite+1) #cheat prend la valeur du reste de la division du nombre d'allumettes par le multiple "suite+1"
        if cheat>0:
            ordiRetire=cheat
            compromis=ordiRetire in got #si une des valeurs que l'ordi veut jouer se trouve dans got alors il ne la jouera pas
            if compromis==False:
                return ordiRetire #retourne la valeur "ordiRetire" si toutes les conditions sont remplies
    return 0 #sinon renvoie 0 et l'ordinateur continue de chercher une valeur.

#############################################################################
################ valeur aléatoire #################################

def valAl(ordiRetire,nbAllum,regleOrdi,taille,got):
    p=0               
    ordiRetire=1000 #ici on veut juste un nombre au dessus de 40 pour rentrer la première fois dans la boucle
    compromis=True
    while p<100 and ordiRetire>nbAllum or compromis==True: #ne pas retirer plus que ce qu'il y a d'allumettes. On limite p à 100 pour éviter de bloquer le jeu si l'ordi est condamné à perdre
        ordiRetire=0
        taille=len(regleOrdi)
        n=random.randint(0,1000) #le programme tire un nombre 
        r=n%taille #on se ramene à la longueur de la règle (cette ligne est équivalente à r=random.randit(0, len(regleOrdi)-1)
        ordiRetire=regleOrdi[r] #r permet de choisir une valeur aléatoire dans la longueur de la règle
        p=p+1
        compromis=ordiRetire in got 
    if p>=99: #si aucune de toutes ces techniques ne fonctionnent apres 100 tirages successifs 
        ordiRetire=random.randint(1,2) #alors l'IA tire aléatoirement une valeur entre 1 et 2
        return ordiRetire
    return ordiRetire

#############################################################################
################# applique la technique de fin de partie (pour "suite" < à 3)#################

def modulo3end(nbAllum,ordiRetire,got):
    cheat=nbAllum%3 #regle du multiple de 3
    compromis=cheat in got #encore une fois si la valeur ne fait pas perdre l'IA
    if cheat==1 and compromis==False:
        ordiRetire=1
        return ordiRetire
    elif cheat==2 and compromis==False:
        ordiRetire=2
        return ordiRetire #retire une valeur pour se ramener à un multiple de 3
    return ordiRetire #si il ne peut pas ordiRetire est toujours égal à 0


#############################################################################
############# applique le plan de jeu général ( pour "suite" < 3) ##############
def modulo3game(nbAllum,ordiRetire,regle,valar,got,suite):
    cheat=nbAllum%3
    m=0
    compromis=cheat in got
    r=1
    while r<3: #on essaie pour r=1 et r=2 car on est en modulo3
        if cheat==r and compromis==False:
            while m<len(regle):
                z=(nbAllum-(regle[m]))%3 
                if z==0:
                    i=regle[m]
                    valar.append(i) # cette boucle ajoute toutes les valeurs de regle
                                   # qui permettent d'appliquer la regle du modulo3 dans la liste "valar"
                m=m+1
            l=len(valar)
            if l>0:
                u=random.randint(0,(l-1)) #Tire une valeur si possible dans la liste valar
                ordiRetire=valar[u]
                compromis2=ordiRetire in got
                if compromis2==False:
                    return ordiRetire
        r=r+1
    return 0

#############################################################################
########## Plan de jeu pour le mode de jeu 1 #############################

def modulo4(nbAllum,ordiRetire):
    cheat=nbAllum%4 # applique la regle du modulo 4
    if cheat==1:
        ordiRetire=1
    elif cheat==2:
        ordiRetire=2
    elif cheat==3:
        ordiRetire=3 #retire un nombre d'allumette(s) pour se ramener à un multiple de 4
    else:
        ordiRetire=random.randint(1,3) #sinon tire une valeur au hasard
    
    return ordiRetire

###############################################################################
####     IA     ####
############################################################################

def IA(nbAllum,regleOrdi,mdj,regle):
    suite=2
    got=[]
    valar=[]
    ordiRetire=0
    taille=len(regleOrdi)    # initialisation des variables dont on aura besoin
    ##regleOrdic=regleOrdi #ne sert qu'à calculer "regleOrdi" à 2 manches différentes : sur le son tour, et celui de l'adversaire
    ##taille2=len(regleOrdic)  #d'où la necessité d'une deuxieme variable égale
    
    
    ordiRetire=checkVictory(regleOrdi,ordiRetire,nbAllum,taille) #le programme peut gagner ?
    if ordiRetire>0:
        return ordiRetire

    if mdj==2: #mode de jeu 2 difficulte 2
        if ordiRetire==0: #si non il joue
            got=Anticipation(regleOrdi,nbAllum,got,taille) #mauvaises valeurs
        suite=regleModulo(suite,regle) #défini son plan de jeu

        ordiRetire=ModuloPlus(regle,nbAllum,ordiRetire,got,suite) #choisi une valeur correct parmi son plan de jeu
        if ordiRetire>0:
            return ordiRetire
        
        if ordiRetire==0: #si aucune des techniques ci dessus permet à l'IA d'effctuer un tour interessant alors on continue           
            p=0               
            if nbAllum<6 and suite<3: #si l'on peut , on applique la regle du modulo 3
                ordiRetire=modulo3end(nbAllum,ordiRetire,got) #en fin de partie
                if ordiRetire>0:
                    return ordiRetire
            elif nbAllum>5 and suite<3: #encore, regle du modulo 3 mais avec des conditions différentes
                ordiRetire=modulo3game(nbAllum,ordiRetire,regle,valar,got,suite)
                if ordiRetire>0:
                    return ordiRetire

            ordiRetire=valAl(ordiRetire,nbAllum,regleOrdi,taille,got) #si finalement il ne peut rien faire il prend un chiffre au hasard
            return ordiRetire
        
    else: #mdj 1 difficulte 2 , si mode de jeu classique
        if nbAllum<4: 
            ordiRetire=checkVictory(regleOrdi,ordiRetire,nbAllum,taille) #assure la victoire si possible
        else:
            ordiRetire=modulo4(nbAllum,ordiRetire) #sinon applique la seule technique possible
        return ordiRetire
