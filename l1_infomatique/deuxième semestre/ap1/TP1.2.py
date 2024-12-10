from random import shuffle
from timeit import timeit
from math import *
from matplotlib import pyplot as plt
"""
>>> l1 = [1, 2, 3, 4]
>>> l2 = l1
>>> l3 = list(l1)
>>> l1==l2
True
>>> l1==l3
True
>>> l2==l3
True

>>> l3[2] = 5
>>> l3
[1, 2, 5, 4]

>>> l1
[1, 2, 3, 4]
>>> l2
[1, 2, 3, 4]

>>> l2
[1, 6, 3, 4]
l1==l2
True
>>> l2==l3
False
>>> l1==l3
False
leq listes l1 et l2 restent égale car les listes l1 et l2 sont les mêmes si l'une subit une modification, l'autre aussi. alors que l3 est
une copie de l1, si une subit une modification, autre ne la subit pas.



>>> l1 = [1, 2, 3, 4]
>>> shuffle(l1)
>>> l1
[3, 4, 1, 2]
>>> l1 = [1, 2, 3, 4]
>>> shuffle(l1)
>>> l1
[2, 4, 1, 3]

q1/ cela renvoie une liste
q2/ elle mélange les élements de la liste de manière aléatoire.
  
"""
def my_shuffle(listee):
    """
    mélange les élements de la liste passée en paramètre de manière aléatoire.
    :param x: (liste) une liste
    :return x:(liste) la même liste mais mélangé
    :CU: None
    
    :exemples:
    >>> my_shuffle([3,2,5])
    [3, 5, 2]
    """
    r = list(listee)
    shuffle(r)
    return r

def construit_liste1(n):
    """
    renvoie la liste des entiers de 0 à n−1.
    :param n:(int) un entier
    :return l:(liste) une liste d'entier par ordre croissant.
    :CU: None
    
    :exemples:
    >>> construit_liste1(4)
    [0, 1, 2, 3]
    """
    l=[]
    for i in range(n):
        l= l+[i]
    return l

def construit_liste2(n):
    """
    renvoie la liste des entiers de 0 à n−1.
    :param n:(int) un entier
    :return l:(liste) une liste d'entier par ordre croissant.
    :CU: None
    
    :exemples:
    >>> construit_liste2(4)
    [0, 1, 2, 3]
    """
    l=[]
    for i in range(n):
        l.append(i)
    return l

def construit_liste3(n):
    """
    renvoie la liste des entiers de 0 à n−1.
    :param n:(int) un entier
    :return l:(liste) une liste d'entier par ordre croissant.
    :CU: None
    
    :exemples:
    >>> construit_liste3(4)
    [0, 1, 2, 3]
    """    
    l=[i for i in range(n)]
    return l

#>>> timeit(stmt='(1+sqrt(3))/2',setup='from math import sqrt',number=1000000)
#0.3958014000000105

LONGUEURS_LISTES = tuple([i for i in range(0,101)])
NOMBRE_EVAL = 100


##temps1
#i = 1
r = [0 for i in range(len(LONGUEURS_LISTES))]
for i in LONGUEURS_LISTES:
   r[i] = timeit(stmt='construit_liste1('+str(i)+')', setup='from __main__ import construit_liste1',number=NOMBRE_EVAL)
   
#for i in LONGUEURS_LISTES:
#   print('i:',i,'val:',r[i])

temps1 = r


##temps2
#i = 1
r = [0 for i in range(len(LONGUEURS_LISTES))]
for i in LONGUEURS_LISTES:
    r[i] = timeit(stmt='construit_liste2('+str(i)+')',setup='from __main__ import construit_liste2',number=NOMBRE_EVAL)

#for i in LONGUEURS_LISTES:
#   print('i:',i,'val:',r[i])

temps2 = r



##temps3
#i = 1
r = [0 for i in range(len(LONGUEURS_LISTES))]
for i in LONGUEURS_LISTES:
    r[i] = timeit(stmt='construit_liste3('+str(i)+')',setup='from __main__ import construit_liste3',number=NOMBRE_EVAL)
#for i in LONGUEURS_LISTES:
#   print('i:',i,'val:',r[i])

temps3 = r

abscisses = LONGUEURS_LISTES
ordonnees1 = temps1
ordonnees2 = temps2
ordonnees3 = temps3
plt.plot(abscisses, ordonnees1, color='blue', label ='Construction 1')
plt.plot(abscisses, ordonnees2, color='red', label ='Construction 2')
plt.plot(abscisses, ordonnees3, color='green', label ='Construction 3')

##Legends
plt.legend(loc='upper left')

plt.show()