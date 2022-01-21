#   FLICK COLOR  
#  Julien Goetghebeur 2020

from random import randint

grille = []
CASE = 50
highScore = 100

nb_clics = 0
clic = False

liste_couleurs = []
liste_couleurs.append(color(0,0,255))
liste_couleurs.append(color(0,255,0))
liste_couleurs.append(color(255,0,0))
liste_couleurs.append(color(0,255,255))
liste_couleurs.append(color(255,0,255))
liste_couleurs.append(color(255,255,0))

ecran = 'titre'

def setup():
    global img_titre
    textAlign(CENTER)
    imageMode(CENTER)
    size(500,500)
    img_titre = loadImage("flickColor-titre3.png")

def draw():
    global ecran
    background(0)
    if ecran == 'titre':
        choix = ecran_titre()
        if choix == 'JOUER':
            initialisation()
            ecran = 'jeu'
        elif choix == 'QUITTER':
            exit()
    elif ecran == 'jeu':
        jeu()
    elif ecran == 'fin':
        choix = ecran_fin()
        if choix == 'REJOUER':
            initialisation()
            ecran = 'jeu'
        elif choix == 'QUITTER':
            exit()

def initialisation():
    global grille, nb_clics, clic
    grille = nouvelle_grille(liste_couleurs)
    nb_clics = 0
    clic = False

def jeu():
    global grille, nb_clics, clic, ecran,highScore
    rectMode(CORNER)
    dessiner_grille(grille)
    if mousePressed:
        if clic is False: # le clique n'est compté que si le joueur ne cliquait pas au dernier passage
            couleur_finale = grille[mouseY/50][mouseX/50]
            colorier(0,0,grille[0][0],couleur_finale)
            nb_clics += 1
        clic = True
    else: 
        clic = False
    if est_unicolor(grille):
        ecran = 'fin'
        if nb_clics < highScore:
            highScore = nb_clics
    
def nouvelle_grille(liste_couleurs, taille = 10):
    """
    Renvoie une grille avec des couleurs choisies aléatoirement dans liste_couleurs
    """
    grille = []
    for i in range(taille):
        grille.append([])
        for j in range(taille):
            couleur = randint(0,5)
            grille[i].append(liste_couleurs[couleur])
    return grille
    
def dessiner_grille(grille):
    """
    Dessine la grille g dans la fenêtre
    """
    global CASE
    for y in range(len(grille)):
        for x in range(len(grille[y])):
            fill(grille[y][x])
            square(x*CASE,y*CASE,CASE)

def colorier(x,y,couleur_initiale,couleur_finale):
    """
    Modifie la couleur de la case (x,y) et de toutes les cases adjacentes vers la droite et vers le bas qui ont la même couleur initiale.
    """
    global grille
    grille[y][x] = couleur_finale
    if x+1 < 10:
        if grille[y][x+1] == couleur_initiale:
            colorier(x+1,y,couleur_initiale,couleur_finale)
    if y+1 < 10:
        if grille[y+1][x] == couleur_initiale:
            colorier(x,y+1,couleur_initiale,couleur_finale)

def est_unicolor(grille):
    """
    Revoie True si la grille n'est remplie que d'une couleur
    """
    for ligne in range(len(grille)):
        if ligne +1 < 10:
            if grille[ligne] != grille[ligne+1]:
                return False
    return True

def bouton(x,y,largeur,hauteur,texte,couleur):
    """
    Créer un bouton avec du texte. il s'agrandit et change de couleur lorsque la souris passe dessus.
    """
    textSize(30)
    if  x-largeur/2< mouseX < x + largeur/2 and  y - hauteur/2< mouseY < y + hauteur/2 :
        fill (couleur[0],couleur[1],couleur[2]+100)
        rect(x,y,largeur+10,hauteur+10,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.28)
        if mousePressed :
            return True
    else:
        fill (couleur[0],couleur[1],couleur[2])
        rect(x,y,largeur,hauteur,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.28)
    return False

def ecran_titre():
    """
    affiche l'écran titre du jeu:
        - image titre
        - bouton JOUER
        - bouton QUITTER
    """ 
    global img_titre
    rectMode(CENTER)
    image(img_titre,width/2,100)
    if bouton(width/2,300,150,50,"JOUER",[0,255,0]):
        return 'JOUER'
    elif bouton(width/2,400,150,50,"QUITTER",[255,0,0]):
        return 'QUITTER'

def ecran_fin():
    """
    affiche l'écran de fin:
        - le score 
        - le meilleur score
        - bouton REJOUER
        - bouton QUITTER
    """
    global nb_clics, highScore
    fill(0,0,255)
    textSize(50)
    text("Partie terminee",width/2,100)
    textSize(30)
    text("Votre score : "+str(nb_clics), width/2,250)
    text("Meilleur score : "+ str(highScore),width/2,300) 
    rectMode(CENTER)
    if bouton(150,400,150,50,"REJOUER",[0,255,0]):
        return 'REJOUER'
    elif bouton(350,400,150,50,"QUITTER",[255,0,0]):
        return 'QUITTER'
    
