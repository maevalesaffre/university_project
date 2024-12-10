#####             TP 4            #####
# Lesaffre Maeva Kernouf Sabrina #


#Import:
from compare import *
from lexique import *
from doctest import DocTest
from functools import cmp_to_key
from timeit import timeit

def est_trie_v1(l, comp=compare):
    '''
    :param l: (str ou tuple ou list) une structure séquentielle
    :param comp: (function) fonction de comparaison
    :return: (bool)
      - True si l est triée selon l'odre défini par comp
      - False sinon
    :CU: éléments de l comparables avec la fonction comp
    :Exemples:

    >>> est_trie([1, 2, 3, 4])
    True
    >>> est_trie([4, 3, 1, 2])
    False
    '''
    listee=[]
    longueur=len(l)
    for i in range(longueur-1):
        c = comp(l[i],l[i+1])
        if c==1:
            listee.append(False)
        else:
            liste.append(True)
    return all(listee)

def est_trie_v2(l, comp=compare):
    '''
    :param l: (str ou tuple ou list) une structure séquentielle
    :param comp: (function) fonction de comparaison
    :return: (bool)
      - True si l est triée selon l'odre défini par comp
      - False sinon
    :CU: éléments de l comparables avec la fonction comp
    :Exemples:

    >>> est_trie([1, 2, 3, 4])
    True
    >>> est_trie([4, 3, 1, 2])
    False
    '''
    long = len(l)
    c = comp(l[0],l[1])
    i = 1
    while not c == 1 and i < long-1:
        c = comp(l[i],l[i+1])
        i += 1
    if c == 1:
        return False
    else: 
        return True
    
l=len(LEXIQUE)
liste=[]
for i in range(l-1):
    if LEXIQUE[i]<LEXIQUE[i+1]:
        liste.append[(i, LEXIQUE[i], LEXIQUE[i+1])]
print(len(liste))


        
    
