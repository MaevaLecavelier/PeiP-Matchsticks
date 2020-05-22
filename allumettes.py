# LECAVELIER Maeva - POUEYTO Clement G2

####################### ATTENTION #################################
# Ce fichier lance le jeu avec de la musique, d'après nos test cela ne fonctionne que sur MAC
#Il y a un autre fichier "allumettes-no-audio.py" qui marche sur toutes les machines.

##### MODULES #####
from codeJeu import *
from turtle import *
from decor import *
from plateau import *
from epee import *
import subprocess
import signal 
import os #ces 3 imports permettent de gérer l'audio
tracer(0)
############################ Affiche les éléments de fin de partie ###############################################
#fonction appelée lorsque la partie est finie
def elemFinal(x_epee,y_epee,nbAllum,long,haut,ordiRetire,regle,n): 
    dessineEpee(x_epee,y_epee,nbAllum,long,haut,ordiRetire,regle) #Ne trace que le plateau car il n'y a plus d'épée car dessineEpee appelle plateau()
    up()
    goto(0,0)
    down()
    if n%2==0:
        color("green")
        write("Vous avez gagné",False,align="center",font=("Arial", 32, "normal"))
        os.system(r'afplay win.wav&') #joue le son de victoire
        
    else:
        color("red")
        write("L'ordinateur a gagné",False,align="center",font=("Arial", 32, "normal"))
        os.system(r'afplay lose.wav&') #joue le son de défaite
        
###############################################################################


#################################################################################
# FONCTION PARTIE #
############################################################################

def JEU(nbAllum,mdj,difficulte,regle,regleOrdi,endgame,ordiRetire,n,long,haut,x_epee,y_epee): # "n" indique qui joue. Pair = joueur, impair = ordi. 
    while endgame==0: #tant que les conditions de victoire ne sont pas réunies
        if n%2==0: #on fait jouer le joueur
            dessineEpee(x_epee,y_epee,nbAllum,long,haut,ordiRetire,regle)#trace le plateau et les épées (selon le nombre d'allumettes) 
            nbAllum=retireAllum(nbAllum,regle,mdj)# retireAllum demande au joueur combien d'épées il veut retirer et met à jour directement le nombre d'épées
            os.system(r'afplay sword_cut.wav&') #lance le son d'épée du joueur
            ordiRetire=0 #on réinitialise la variable d'ordiRetire. Utilité dans la fonction dessineEpee
            dessineEpee(x_epee,y_epee,nbAllum,long,haut,ordiRetire,regle)#affiche le nouveau nombre d'épées
            endgame=jeuValide(nbAllum) #vérifie si le jeu continue
            if endgame==1: #si la partie se finit
                elemFinal(x_epee,y_epee,nbAllum,long,haut,ordiRetire,regle,n)


        else:    #l'ordinateur joue
            textinput(" ","Au tour de l'ordinateur ? ")#marque une pause
            if difficulte==1:
                ordiRetire=ordinateurFacile(regleOrdi,nbAllum,mdj)
            else:   #difficulté 2
                ordiRetire=IA(nbAllum,regleOrdi,mdj,regle)
            nbAllum=playOrdinateur(nbAllum,ordiRetire)
            os.system(r'afplay sword_ia.wav&')
            endgame=jeuValide(nbAllum) #vérifie si le jeu continue
            if endgame==1:
                elemFinal(x_epee,y_epee,nbAllum,long,haut,ordiRetire,regle,n)
        n=n+1 #change de tour
        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
musique=os.system(r'afplay got_theme1.wav&') #joue musique de fond
paysage() #affiche le paysage fixe
rejouer=1
while rejouer==1:
    mdj=0
    difficulte=0

    while mdj<1 or mdj>2: #le joueur séléctionne le mode de jeu
        mdj=int(numinput("MODE DE JEU","Choisissez un mode de jeu : 1 - Classique / 2 - Aléatoire ",2,1,2)) #affiche la fenetre de discussion avec le l'utilisateur
    while difficulte<1 or difficulte>2: #le joueur selectionne la difficulté
        difficulte=int(numinput("DIFFICULTE","Choisissez une difficulté : 1 - Facile / 2 - Difficile ",2,1,2))
        
    nbAllum=modeDeJeu(mdj,nbAllum) #tire un nombre d'allumettes de départ
    regle=regleAleatoire(mdj) #crée les règles de la partie
    regleOrdi=regle #les règles pour l'ordinateur
    JEU(nbAllum,mdj,difficulte,regle,regleOrdi,endgame,ordiRetire,n,long,haut,x_epee,y_epee) #lance le jeu
    rejouer=int(numinput("Une autre partie ?", "Voulez-vous rejouer ? OUI : 1, NON : 2", 1,1,2))
os.kill(musique, signal.SIGKILL) #ferme le programme ainsi que la musique de fond (commande trouvée sur un forum utilisable que sur MAC)


