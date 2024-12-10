import numpy as np

g = np.array([[0,1,1,0],[1,0,1,0],[1,1,0,0],[0,0,0,0]])

g = np.array(
    [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ])


def testSommetConnect(graphe, ligne, colonne):
    if(graphe[ligne][colonne] == 1) :
        return True
    else :
        return False
    
def voisins(graphe, sommet):
    """
    Retourne la liste des successeurs du sommet dans le graphe.
    CU: le sommet existe
    """
    voisins = []
    for i in range(len(graphe[sommet])):
        if(graphe[sommet][i] == 1):
            voisins.append(i)
    return voisins 
        


def taille(graphe):
    i = 0
    sommet = list()
    for sommet in graphe :
        for arrete in sommet :
            if arrete == 1 :
                i +=1
    return i/2
        
def ajouter_arete (graphe, sommet1, sommet2):
    graphe[sommet1][sommet2] = 1
    graphe[sommet2][sommet1] = 1
    
    
    
    
    

    
