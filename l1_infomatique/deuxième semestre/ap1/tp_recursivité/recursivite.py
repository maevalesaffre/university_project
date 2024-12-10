#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Noms: Lesaffre 
# Prenoms : Maeva
# Groupe :12
# Date :29/03/2020



"""

:mod: module `recursivite`
:author: FIL - Faculté des Sciences et Technologies - Univ. Lille
:link: <http://portail.fil.univ-lille1.fr>_
:date: Mars 2020
:dernière révision: Mars 2020

"""

from ap2_decorators import count, trace


def taille_binaire(naturel):
    """
    calcule le nombre de chiffres dans l'écriture binaire de l'entier naturel `naturel`

    :param naturel: (int)
    :return: (int)
    :CU: naturel >= 0
    :ExU:
    >>> taille_binaire(0)
    1
    >>> taille_binaire(1)
    1
    >>> taille_binaire(2)
    2
    >>> taille_binaire(1023)
    10
    >>> taille_binaire(1024)
    11
    >>> from random import randrange
    >>> l = [randrange(1,2**100)  for _ in range(100)]
    >>> all(taille_binaire(elt) == len(bin(elt))-2  for elt in l)
    True

    """
    res = 1
    while naturel >= 2:
        res += 1
        naturel //= 2
    return res

def taille_binaire_recursive(naturel):
    """
    calcule le nombre de chiffres dans l'écriture binaire de l'entier naturel `naturel`

    :param naturel: (int)
    :return: (int)
    :CU: n >= 0
    :ExU:

    >>> taille_binaire_recursive(0)
    1
    >>> taille_binaire_recursive(1)
    1
    >>> 
    2
    >>> taille_binaire_recursive(1023)
    10
    >>> taille_binaire_recursive(1024)
    11
    >>> from random import randrange
    >>> l = [randrange(1,2**100)  for _ in range(100)]
    >>> all(taille_binaire_recursive(elt) == len(bin(elt))-2  for elt in l)
    True

    """
    res=1
    if naturel >= 2:
        res= 1 + taille_binaire_recursive(naturel // 2)
    return res

def poids_binaire(naturel):
    """
    calcul le nombre de chiffre 1 dans l'écriture binaire de l'entier naturel `naturel`

    :param naturel: (int)
    :return: (int)
    :CU: naturel >= 0
    :ExU:

    >>> poids_binaire(0)
    0
    >>> poids_binaire(1)
    1
    >>> poids_binaire(2)
    1
    >>> poids_binaire(255)
    8
    >>> from random import randrange
    >>> l = [randrange(1,2**100)  for _ in range(100)]
    >>> all([poids_binaire(x)==bin(x).count('1') for x in l])
    True

    """
    res = naturel % 2
    while naturel > 0:
        naturel //= 2
        res += naturel % 2
    return res


def poids_binaire_recursif(naturel):
    """
    calcul le nombre de chiffre 1 dans l'écriture binaire de l'entier naturel `naturel`

    :param naturel: (int)
    :return: (int)
    :CU: n>=0
    :ExU:

    >>> poids_binaire_recursif(0)
    0
    >>> poids_binaire_recursif(1)
    1
    >>> poids_binaire_recursif(2)
    1
    >>> poids_binaire_recursif(255)
    8
    >>> from random import randrange
    >>> l = [randrange(1, 2**100)  for _ in range(100)]
    >>> all([poids_binaire_recursif(x)==bin(x).count('1') for x in l])
    True

    """
    res= naturel % 2
    if naturel >=2:
        res= naturel%2+ poids_binaire_recursif(naturel//2)
    return res
    
def puissance(x, n):
    """
    calcule  x élevé à la puissance n

    :param x: (int or float)
    :param n: (int)
    :return: (int or float)
    :CU: n>=0
    :ExU:

    >>> puissance(10, 0)
    1
    >>> puissance(10, 1)
    10
    >>> puissance(2, 10)
    1024

    """
    res= x**n
    return res

def puissance_v2(x, n):
    """
    calcule  x élevé à la puissance n

    :param x: (int or float)
    :param n: (int)
    :return: (int or float)
    :CU: n >= 0
    :ExU:

    >>> puissance_v2(10,0)
    1
    >>> puissance_v2(10,1)
    10
    >>> puissance_v2(2,10)
    1024

    """
    if n == 0:
        res= 1
    else:
        res= x*puissance_v2(x,n-1)
    return res   

@count
def fois(x, y):
    """
    renvoie le produit de x par y

    :param x: (int or float)
    :param y: (int or float)
    :return: (int or float)
    :CU: les mêmes que l'opérateur *

    :ExU:
    >>> fois(8, 7)
    56

    """
    return x * y

#q6
#le type du paramètre puissance, c'est une fonction
#le type de res est une liste
def comptage(puissance):
    """ fabrique une liste de longueur 100 contenant
        le nombre de multiplications effectuées par la
        fonction ``puissance`` passée en paramètre

        :param puissance: (function)
        :return: (list)
        :CU: la fonction doit être implantée en
             utilisant la fonction ``fois``

    """
    res = []
    for i in range(100):
        fois.counter = 0
        _ = puissance(2, i)
        res.append(fois.counter)
    return res
#q7
#>>> comptage(puissance)
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#>>> comptage(puissance_v2)
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#@trace
def puissance_calbuth(x, n):
    """
    calcule  x élevé à la puissance n

    :param x: (int or float)
    :param n: (int)
    :return: (int or float)
    :CU: n>=0
    :ExU:

    >>> puissance_calbuth(10,0)
    1
    >>> puissance_calbuth(10,1)
    10
    >>> puissance_calbuth(2,10)
    1024

    """
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        k = n // 2
        return puissance_calbuth(x, k) * puissance_calbuth(x, n - k)
#q11
#>>> puissance_calbuth(2,5)
# -> puissance_calbuth((2, 5), {})
#... -> puissance_calbuth((2, 2), {})
#...... -> puissance_calbuth((2, 1), {})
#...... <- 2
#...... -> puissance_calbuth((2, 1), {})
#...... <- 2
#... <- 4
#... -> puissance_calbuth((2, 3), {})
#...... -> puissance_calbuth((2, 1), {})
#...... <- 2
#...... -> puissance_calbuth((2, 2), {})
#......... -> puissance_calbuth((2, 1), {})
#......... <- 2
#......... -> puissance_calbuth((2, 1), {})
#......... <- 2
#...... <- 4
#... <- 8
# <- 32
#32    

#>>> puissance_calbuth(2,2)
# -> puissance_calbuth((2, 2), {})
#... -> puissance_calbuth((2, 1), {})
#... <- 2
#... -> puissance_calbuth((2, 1), {})
#... <- 2
# <- 4
#4

#puissance_calbuth(2,2) est calculé 4 fois

def puissance_calbuth_v2(x, n):
    """
    calcul de x élevé à la puissance n

    :param x: (int or float)
    :param n: (int)
    :return: (int or float)
    :CU: n>=0
    :ExU:

    >>> puissance_calbuth_v2(10,0)
    1
    >>> puissance_calbuth_v2(10,1)
    10
    >>> puissance_calbuth_v2(2,10)
    1024

    """
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        k = n // 2
        return fois(puissance_calbuth(x, k), puissance_calbuth(x, n - k))
   
#q9
#q10
     
def puissance_calbuth_v2_amelioree(x, n):
    """
    calcul de x élevé à la puissance n

    :param x: (int or float)
    :param n: (int)
    :return: (int or float)
    :CU: n>=0
    :ExU:

    >>> puissance_calbuth_v2_amelioree(10,0)
    1
    >>> puissance_calbuth_v2_amelioree(10,1)
    10
    >>> puissance_calbuth_v2_amelioree(2,10)
    1024

    """
    if n==0:
        return 1
    if n%2 ==0:
        m=puissance_calbuth_v2_amelioree(x, n/2)
        return m*m
    else:
        return x*puissance_calbuth_v2_amelioree(x, n-1)



def puissance_erronee(x, n):
    """
    aurait dû calculer  x élevé à la puissance n

    :param x:(int or float)
    :param n:(int)
    :return (int or float)
    :CU: n >= 0

    :ExU:
    >>> puissance_erronee(10, 0)
    1
    >>> puissance_erronee(10, 1)
    10
    >>> #>>> puissance_erronee(2, 10)
    >>> #1024

    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        r = n % 2
        q = n // 2
        return puissance_erronee(x, r) * puissance_erronee(puissance_erronee(x, q), 2)


def puissance_reparee(x, n):
    """
    aurait dû calculer  x élevé à la puissance n

    :param x:(int or float)
    :param n:(int)
    :return (int or float)
    :CU: n>=0

    :ExU:
    >>> puissance_reparee(10,0)
    1
    >>> puissance_reparee(10,1)
    10
    >>> puissance_reparee(2,10)
    1024

    """
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        r= n%2
        q=n//2
        if r==0:
            return puissance_calbuth(puissance_calbuth(x,q),2)
        else:
            return fois(x,puissance_calbuth(puissance_calbuth(x, (n-1//2)),2))

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                    verbose=True)
