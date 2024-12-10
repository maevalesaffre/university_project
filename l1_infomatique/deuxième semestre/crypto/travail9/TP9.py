#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
:auteur 1: Lesaffre Maeva
:auteur 2: Kernouf Sabrina
:groupe: SESI 12
:date: vendredi 27 mars 2020
:objet: Travail numéro 9 (Nombres premiers et témoins de Fermat)
"""

from matplotlib import pyplot as plt
from math import log
from random import randrange
from tp1 import *
from tp6_arithmetique import *


# n_max = 10000
# n = 2
# for n in range(n_max):
#     if not est_premier2(n) and all(pow(a,n,n)==a for a in range(n)): 
#         print(n)
        

def expo_mod_rapide(a, b, N):
    """
    :param int a:
    :param int b: exposant
    :param int n: modulus
    :return: r dans {0, 1, ..., n-1} tel que a^b = r (mod n)
             calcul effectué par l'exponentiation rapide.
    :rtype: int
    :CU: b >= 0, n > 0
    :Exemples:

    >>> expo_mod_rapide(2, 10, 100)
    24
    >>> expo_mod_rapide(14, 3141, 17)
    12
    """
    return pow(a, b, N)


def est_temoin_non_primalite(a, n):
    ''':param int a, n:
    :return:
        - True si a est un témoin de non primalité de n
        - False sinon
    :rtype: bool
    :CU: n > 1

    Ça serait mieux d'utiliser une variante
    est_temoin_non_primalite_variante() qui ne vérifierait pas le pgcd :
    car de toute façon si le pgcd ne vaut pas 1, le test d'exponentation
    modulaire ne peut pas donner une valeur égale à 1, pour n > 2.

    En effet si x ** (n-1) vaut 1 modulo n alors x ** (n - 1)
    est premier avec n donc AUSSI x, et sans avoir calculé le pgcd(x, n)
    on saura qu'il vaut 1.

    Autrement dit :

    Si on s'aperçoit que x ** (n-1) (modulo n) ne vaut pas 1, alors soit
    x (avec 1 <= x < n) a un facteur commun avec n, et donc n n'est pas
    premier, soit x n'a pas de facteur commun avec n et donc n n'est pas
    premier par la contraposée du théorème de Fermat. Il est donc idiot
    de calculer ce pgcd, on le fait uniquement pour être dans le cadre
    de la définition du texte de ce qu'est un témoin de Fermat.

    Bien sûr il faut alors s'assurer que la variable a (que j'ai notée x
    dans le paragraphe ci-dessus) donne une classe de congruence
    non-nulle modulo n, donc il faut rajouter la CU que a % n n'est pas
    nul.

    >>> n = 2**32 + 1
    >>> est_temoin_non_primalite(2, n)
    False
    >>> est_temoin_non_primalite(3, n)
    True

    '''
    return pgcd(a, n) == 1 and expo_mod_rapide(a, n-1, n) != 1


# Exercice

# Trouvez l'entier inférieur à 10000 dont le nombre de témoins de non
# primalité est relativement le plus grand, i.e. telle que la fréquence de ce
# nombre de témoins nbre temoins/(n−2) est la plus grande. Même question avec
# la fréquence la plus petite mais non nulle.

# n_max = n_min = 4
# max_temoins = min_temoins = len(liste_temoins(4))/(4-2)
# for n in range(5, 10001):
#     freq_temoins = len(liste_temoins(n))/(n-2)
#     if 0 < freq_temoins < min_temoins:
#         n_min = n
#         min_temoins = freq_temoins
#     elif max_temoins < freq_temoins:
#         n_max = n
#         max_temoins = freq_temoins
# ((n_min, min_temoins), (n_max, max_temoins))


def est_carmichael(n):
    '''
    :param int n:
    :return:
       - True si n est un nombre de Carmichael
       - False sinon
    :rtype: bool
    :CU: n > 0
    :Exemples:
    
    >>> any(est_carmichael(k) for k in range(1, 561))
    False
    >>> est_carmichael(561)
    True
    '''
    fact = factorise(n)
    r = len(fact)
    return (r > 1 and
            all(fact[i][1] == 1 for i in range(r)) and
            all((n - 1) % (fact[i][0] - 1) == 0 for i in range(r)))


# Exercice :
#
# La décomposition en facteurs premiers des nombres de Carmichael comprend au
# moins trois facteurs premiers. Trouvez tous les nombres de Carmichael
# produits de trois nombres premiers inférieurs à 1000. Combien y en a-t-il ?
#
# lp = eratosthene(1000)
# nlp = len(lp)
# liste_carmichael_3_facteurs_premiers =[lp[i]*lp[j]*lp[k] for i in range(nlp)
#                    for j in range(i+1, nlp) 
#                    for k in range(j+1, nlp)
#                    if est_carmichael(lp[i]*lp[j]*lp[k])]
# len(liste_carmichael_3_facteurs_premiers)

def nbre_fermat(n):
    return 2 ** (2 ** n)


def est_compose(n, nbre_essais=20):
    ''':param int n:
    ;param int nbre_essais: nbre maximal de tentatives de trouver
                            un témoin de non primalité
    :return:
       - True si un témoin de non primalité a été trouvé
       - False sinon
    :rtype: bool
    :CU: n > 2

    ATTENTION : cette procédure et donc le doctest sont un peu lents à
    cause des calculs de pgcd dans est_temoin_non_primalite


    >>> len([n for n in range(8, 15) if not est_compose(nbre_fermat(n), 5) for n in range(8, 15)])
    0

    '''
    # a = randrange(2, n)
    # essai = 0
    # while essai <= nbre_essais and not est_temoin_non_primalite(a, n):
    #     a = randrange(2, n)
    #     essai += 1
    # return essai < nbre_essais
    for essai in range(nbre_essais):
        a = randrange(2, n)
        if est_temoin_non_primalite(a, n):
            return True
    return False


# Exercice: Existe-t-il un nombre de Fermat Fn, avec 8≤n≤14 qui soit premier ?
# [(n, est_compose(nbre_fermat(n))) for n in range(8, 15)]

# Exercice : Utilisez le prédicat est_compose pour trouver un nombre
# (probablement) premier ayant 30 chiffres.

# n = randrange(10**29, 10**30-2)
# if n % 2 == 0: n += 1
# while est_compose(n):
#     n = randrange(10**29, 10**30-2)
#     if n % 2 == 0: n += 1
# n


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
