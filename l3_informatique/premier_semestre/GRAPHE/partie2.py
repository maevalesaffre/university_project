import numpy as np

g = [[1,2],[0,2],[0,1],[]]


def taille (graphe):
    i = 0
    for sommet in graphe :
        i += len(sommet)
    return i/2
        

def ajouter_arete (graphe, sommet1, sommet2):
    graphe[sommet1].append(sommet2)
    graphe[sommet2].append(sommet1)
    
    