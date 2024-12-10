#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Groupe 12 -- Travail numéro 1

17 janvier 2020

NOM 1: <LESAFFRE Maeva>

NOM 2: <KERNOUF Sabrina>
"""


def mon_divmod(a, b):
    """La fonction divmod() « à la main »

    :param int a: l'entier relatif à diviser
    :param int b: l'entier non nul servant de diviseur
    :CU: b doit être non nul
    :return: si b>0, le quotient et le reste dans la division euclidienne
             de a par b.

             si b<0, le reste renvoyé vérifie -b<r<=0 et le quotient q est
             toujours tel que a = bq + r.
    :rtype: un tuple de deux entiers

    Avec ces définitions, il est toujours vrai que le reste est invariant si
    l'on ajoute à a un multiple (positif ou négatif) quelconque de b. Par
    contre le reste est du même signe que b, contrairement à la définition
    mathématique usuelle qui impose un reste toujours positif ou nul, quel que
    soit le signe (non nul) de b.

    L'avantage de la définition de Python pour b<0 est que le quotient est
    déterminé par la fraction a/b, indépendamment du signe de b, en lui
    appliquant la fonction « partie entière » (math.floor() en Python).

    La procédure mon_divmod n'utilise que des additions et soustractions et ne
    tient pas compte de la remarque précédente.

    >>> mon_divmod(33, 0)
    Traceback (most recent call last):
    AssertionError: Le diviseur doit être non-nul !
    >>> mon_divmod(33, 7)
    (4, 5)
    >>> mon_divmod(-33, 7)
    (-5, 2)
    >>> mon_divmod(33, -7)
    (-5, -2)
    >>> mon_divmod(-33,-7)
    (4, -5)
    >>> mon_divmod(13891638, 317981) == divmod(13891638, 317981)
    True
    >>> mon_divmod(13891638, -317981) == divmod(13891638, -317981)
    True
    >>> mon_divmod(-13891638, 317981) == divmod(-13891638, 317981)
    True
    >>> mon_divmod(-13891638, -317981) == divmod(-13891638, -317981)
    True
    """
    assert b != 0, "Le diviseur doit être non-nul !"
    if b < 0:
        q, r = mon_divmod(-a, -b)
        return (q, -r)
    q = 0
    while a < 0:
        a = a + b
        q = q - 1
    while a >= b:
        a = a - b
        q = q + 1
    return (q, a)


def pgcd(a, b):
    """Calcule le PGCD des entiers relatifs a et b

    On remplace a et b par leurs valeurs absolues, puis
    on implémente l'algorithme d'Euclide :

    - tant que b est non nul, remplacer a par b et b par le reste
      dans la division euclidienne de a par b

    - lorque b est devenu nul, renvoyer a.

    :param int a: un entier naturel relatif
    :param int b: un autre entier naturel relatif
    :return: leur Plus Grand Commun Diviseur.
    :rtype: int
    :CU: aucune.

    >>> pgcd(0, 0)
    0
    >>> pgcd(33, 297)
    33
    >>> pgcd(33, 407)
    11
    >>> pgcd(-1000, -520)
    40
    >>> pgcd(236157846, 5405677)
    17
    """
    a, b = abs(a), abs(b)
    while b > 0:
        a, b = b, a % b
    return a  
        
    
def ppcm(a, b):
    """Calcule le PPCM des entiers relatifs a et b

    Par définition PPCM(0, 0) est 0.
    
    Sinon, on peut l'obtenir par la formule :math:`|ab| = PGCD(a,b)PPCM(a,b)`.

    :param int a: un entier relatif
    :param int b: un second entier relatif
    :return: leur Plus Petit Commun Multiple (toujours positif ou nul)
    :rtype: int
    :CU: aucune.

    >>> ppcm(0, 0)
    0
    >>> ppcm(33, 297)
    297
    >>> ppcm(33, 407)
    1221
    >>> ppcm(-1000, -520)
    13000
    >>> ppcm(236157846, 5405677)
    75093708028926
    """
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    return (a * b) // pgcd(a, b)


def inverse_modulaire_naïf(a, N):
    """Détermine l'inverse multiplicatif de a modulo N

    Renvoie une erreur si a n'est pas premier avec N

    L'algorithme :

    - si le pgcd(a, N) n'est pas 1, lever une exception (voir le doctest)

    - sinon, on sait que l'inverse existe, on le trouve en multipliant tous
      les entiers de 0 à N - 1 jusqu'à en trouver un qui fonctionne.

    Attention au cas particulier N = 1. Dans ce cas on doit renvoyer 0.

    :param int a: un entier relatif
    :param int N: un entier strictement positif, le « modulus »
    :return: un entier b avec 0<= b < N et a fois b congru à 1 modulo N
    :rtype: int
    :CU: N > 0

    >>> inverse_modulaire_naïf(13, -5)
    Traceback (most recent call last):
    AssertionError: Le modulus doit être strictement positif !
    >>> inverse_modulaire_naïf(30, 100)
    Traceback (most recent call last):
    AssertionError: L'entier n'est pas inversible modulo le modulus !
    >>> inverse_modulaire_naïf(31, 100)
    71
    >>> inverse_modulaire_naïf(-10069, 100)
    71
    >>> inverse_modulaire_naïf(71, 100)
    31
    >>> inverse_modulaire_naïf(-10029, 100)
    31
    >>> inverse_modulaire_naïf(31, 1234)
    1035
    >>> inverse_modulaire_naïf(3503, 1234)
    31
    >>> inverse_modulaire_naïf(3503, 3)
    2
    >>> inverse_modulaire_naïf(3503, 2)
    1
    >>> inverse_modulaire_naïf(3503, 1)
    0
    """
    assert N > 0, "Le modulus doit être strictement positif !"
    d=pgcd(a,N)
    assert d==1, "L'entier n'est pas inversible modulo le modulus !"
    for b in range(1,N):
        if a * b % N == 1:
            return b
    return 0

def pgcd_étendu(a, b):
    """Calcule des coefficients u et v de Bézout: pgcd(a,b) = au + bv

    :param int a: un entier relatif
    :param int b: un second entier relatif
    :return: un triplet (d, u, v) avec d le pgcd, et au+bv=d
    :rtype: tuple
    :CU: aucune.

    Le pgcd est toujours positif et la routine doit savoir gérer des entrées
    négatives. Pour cela on notera sa = -1 si a<0, +1 sinon, et sb = -1 si b<0
    et +1 sinon. On calcule d, u, v pour abs(a) et abs(b) et on remplace u par
    sa*u, v par sb*v à la fin.

    Algorithme pour a et b strictement positifs :

    On utilise des variables supplémentaires U, u, V, v qui valent 1, 0, 0, 1
    au départ.

    On calcule q et r par la division euclidienne de a par b.

    - si le reste r est non-nul, on remplace

        a par b, b par r, U par u, u par U - q*u, V par v, v par V - q*v

      attention que ces remplacements doivent être effectués simultanément.
      Puis on recommence.

    - si le reste r est trouvé nul, on renvoie b, u, v

    >>> pgcd_étendu(0, 0)
    (0, 0, 0)
    >>> pgcd_étendu(-2, 1)
    (1, 0, 1)
    >>> pgcd_étendu(2, -1)
    (1, 0, -1)
    >>> pgcd_étendu(-35, 0)
    (35, -1, 0)
    >>> pgcd_étendu(0, 35)
    (35, 0, 1)
    >>> pgcd_étendu(105, 231)
    (21, -2, 1)
    >>> pgcd_étendu(-231, 105)
    (21, -1, -2)
    >>> pgcd_étendu(-231, -105)
    (21, -1, 2)
    >>> pgcd_étendu(236157846, 5405677)
    (17, 158294, -6915391)
    >>> pgcd_étendu(13891638, 317981)
    (1, 158294, -6915391)
    """
    if b==0:
        if a==0:
            return 0,0,0
        return abs(a), -1 if a < 0 else 1, 0
    a, sa = abs(a), -1 if a < 0 else 1
    b, sb = abs(b), -1 if b < 0 else 1
    U, V, u, v = 1, 0, 0, 1
    q, r = divmod(a, b)
    while r:
        a, b = b, r
        U, u = u, U - q * u
        V, v = v, V - q * v
        q, r = divmod(a, b)
    return b, sa * u, sb * v
            
def inverse_modulaire(a, N):
    """Détermine l'inverse multiplicatif de a modulo N

    Renvoie une erreur si a n'est pas premier avec N

    On utilise une identité de Bézout : d = au + Nv

    - si le pgcd d n'est pas 1, lever une exception (voir le doctest)

    - sinon, renvoyer u % N.

    :param int a: un entier relatif
    :param int N: un entier strictement positif, le « modulus »
    :return: un entier b avec 0<= b < N et a fois b congru à 1 modulo N
    :rtype: int
    :CU: N > 0

    >>> inverse_modulaire(13, -5)
    Traceback (most recent call last):
    AssertionError: Le modulus doit être strictement positif !
    >>> inverse_modulaire(30, 100)
    Traceback (most recent call last):
    AssertionError: L'entier n'est pas inversible modulo le modulus !
    >>> inverse_modulaire(31, 100)
    71
    >>> inverse_modulaire(-10069, 100)
    71
    >>> inverse_modulaire(71, 100)
    31
    >>> inverse_modulaire(-10029, 100)
    31
    >>> inverse_modulaire(31, 1234)
    1035
    >>> inverse_modulaire(3503, 1234)
    31
    >>> inverse_modulaire(3503, 3)
    2
    >>> inverse_modulaire(3503, 2)
    1
    >>> inverse_modulaire(3503, 1)
    0
    """
    assert N > 0, "Le modulus doit être strictement positif !"
    D, u, v = pgcd_étendu(a, N)
    assert D == 1, "L'entier n'est pas inversible modulo le modulus !"
    return u % N


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
