from random import randint
# pour importer les fonctions lire_donnees et sauver_resu
from litEcritFichiers import * 

# construction du plateau de jeu

def placer(esp,nav):
    """
    dict, tuple -> NoneType
    place le navire nav dans l'espace maritime esp.
    Choix de l'emplacement aléatoire.

    CU : il doit rester de la place

    Algorithme :
    On va créer une liste de toutes les positions possibles du bateau
    puis on tirera au sort une de ces positions.
    Si'il n'y a plus de place pour ce navire, la liste sera vide et
    le programme plantera

    """
    largeur=esp['larg']
    hauteur=esp['haut']
    longueur=nav[1]
    pos_possibles=[]
    # i=colonne
    for i in range(largeur):
        # j= ligne
        for j in range(hauteur):
            # Pour chaque case où peut commencer le bateau nav
            # on regarde si les cases dans la direction de placement sont libres
            # d'abord à l'horizontale
            # Le bateau doit avoir assez de place à droite
            if(largeur-i>=longueur):
                casesOk=[None for k in range(longueur)]
                for k in range(longueur):
                    casesOk[k]=(not (j,i+k) in esp)
                print("\t",casesOk) 
                if all(casesOk):
                    pos_possibles.append(('H',j,i))
            # puis les verticales
            # le bateau doit avoir assez de place en dessous
            if (hauteur-j>=longueur):
                casesOk=[None for k in range(longueur)]
                for k in range(longueur):
                    casesOk[k]=(not (j+k,i) in esp)
                if all(casesOk):
                    pos_possibles.append(('V',j,i))
    print(pos_possibles)
    print("\n")
    # choisir un placement (tirage aleatoire d'un élément de la liste)
    # Si la liste est vide, on aura une erreur
    choix=randint(0,len(pos_possibles)-1)
    valeur=pos_possibles[choix]
    print("le choix ->",valeur)
    # ajouter les cases occupées par le bateau à l'espace maritime
    # case de depart
    ligne=valeur[1]
    colonne=valeur[2]
    dir=valeur[0]
    if dir=='H':
        for i in range(longueur):
            esp[(ligne,colonne+i)]=nav[0]
    else:
         for i in range(longueur):
            esp[(ligne+i,colonne)]=nav[0]
    print("espace ")
    print(esp,len(esp))
    
def cree_jeu (descr):
    """
    str -> dict
    renvoie un nouveau jeu de bataille navale construit à partir des données 
    lues dans le fichier descr.


    Le jeu est représenté par un dictionnaire à quatre clés :
    - 'plateau' pour représenter le plateau de jeu (l'espace maritime) avec ses navires
    - 'nb_cases_occupees' dont la valeur associée est le nombre de cases du plateau
                          occupées par les navires
    - 'touches' dictionnaire contenant deux champs :
                * l'un nomme 'nb_touches' contenant un entier 
                * l'autre nomme 'etats_navires' qui contient un dictionnaire
                  donnant pour chaque navire le nombre de tirs 
                  qu'ils peuvent encore recevoir avant d'être coulés
    - 'coups_joues' ensemble des coups joués depuis le début de la partie.

    CU : le fichier doit contenir une description correcte du jeu (cf lire_donnees)
    """
    largeur,hauteur,liste_bateaux=lire_donnees(descr)
    espace={'larg':largeur,'haut':hauteur}
    nbcases=0
    states=dict()
    for nave in liste_bateaux:
        nbcases=nbcases+nave[1]
        states[nave[0]]=nave[1]
        placer(espace,nave)
    # Tous lesbateaux sont placés, ou bien le programme a planté si
    # il n'a pas trouvé de solution (quand les premiers bateaux placés bloquent
    # les positions possibles des suivants)
    # finir de construire le jeu
    jeu={'plateau':espace,'nb_cases_occupees':nbcases,'touches':{'nb_touches':0,'etats_navires':states},'coups_joues':set()}
    return jeu        

def decrire_le_jeu(jeu):
    print("Dimensions du plateau de jeu : ")
    print("- largeur : ",jeu['plateau']['larg'])
    print("- hauteur : ",jeu['plateau']['haut'])
    print("Navires :")
    for bato in jeu['touches']['etats_navires']:
        print("- ",bato," : ",jeu['touches']['etats_navires'][bato]," case(s)")
        
    

if __name__ == '__main__':
   resu=cree_jeu(2)
   decrire_le_jeu(resu)
   
   
   
               
            
