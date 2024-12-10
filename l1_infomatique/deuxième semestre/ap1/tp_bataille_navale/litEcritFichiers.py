from datetime import datetime

# fonctions de lecture et d'ecriture
def lire_donnees(n):
    fichier=open("jeu"+str(n)+".txt")
    lignes=fichier.readlines()
    # Dimensions du jeu (première ligne)
    premiereligne=lignes[0]
    # supprimer le caractère de fin de ligne
    premiereligne=lignes[0][:-1]
    # dimensions est une liste de deux chaines de caractères représentant des nombres
    dimensions=premiereligne.split(":")
    # transformer les chaines de caractères en nombres
    dimensions=[int(v) for v in dimensions]
    
    largeur=dimensions[0]
    hauteur=dimensions[1]
    # lecture des lignes suivantes
    #chaque ligne est la description d'un bateau et de sa dimension
    liste_des_bateaux=[]
    for desc in lignes[1:]:
        # traiter une ligne
        #enlever le caractère passage à la ligne
        desc=desc[:-1]
        data=desc.split(":")
        liste_des_bateaux.append((data[0],int(data[1])))
  
    return(largeur,hauteur,liste_des_bateaux)

# sauvegarde du résultat de la partie
def sauver_result(nom,descr,nbr_tirs):
    # ouvrir un fichier en mode 'append' : ecrire les nouvelles valeurs
    # à la suite des précédentes
    fichier=open("FICHIER_RESU",'a')
    # construction de la ligne
    chaine_info=nom+":"+descr+":"+str(nbr_tirs)+":"+str(datetime.today())+"\n"
    fichier.write(chaine_info)
    # ne pas oublier de fermer le fichier
    fichier.close()
    

    

if __name__ == '__main__':
    u=lire_donnees(1)
    print(u)
    sauver_result("surcouf","1",50)
