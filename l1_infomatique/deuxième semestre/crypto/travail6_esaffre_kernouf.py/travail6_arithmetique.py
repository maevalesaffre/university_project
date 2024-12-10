#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
:étudiant 1: Lesaffre maeva
:étudiant 2: Kernouf Sabrina
:groupe: SESI 12 
:date: vendredi 21 février 2020 
:objet: Travail numéro 6 (partie arithmétique : nombres premiers)
"""

import timeit


def eratosthene(N):
    """Le crible d'Ératosthène pour trouver les nombres premiers inférieurs
    ou égaux à une grandeur donnée

    :param int N: un entier
    :return: la liste, dans l'ordre croissant, des nombres premiers
             inférieurs ou égaux à N.
    :rtype: list
    :CU: N est positif ou nul.

    >>> eratosthene(1)
    []
    >>> eratosthene(3)
    [2, 3]
    >>> eratosthene(19)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> len(eratosthene(100)) == 25
    True
    """
    if N <= 1:
        return []
    if N == 2:
        return [2]
    # donc on a N au moins égal à 3 pour la suite
    L = [True] * (N + 1)  # car on veut que L[0], ..., L[N] existent
    L[0] = False
    L[1] = False
    n = 2
    L[2::2] = [False] * (N // 2)  # il y a N//2 indices x avec 2 <= 2*x <= N
    L[2] = True
    n = 1
    # la boucle est organisée de manière très bizarre afin de minimiser
    # les calculs...
    while True:
        n += 2
        if not L[n]:
            # ce n a déjà été éliminé par le crible, il est composé.
            #
            # Mais court-on le risque d'un index out-of-range à la prochaine
            # itération qui sera avec n + 2 ? peut-on avoir n + 2 > N ?
            #
            # Comme on n'est pas sorti avant, on avait pour n-2 que q > n - 2,
            # or N >= q*(n-2) et donc N > (n-2)^2. (si n==3, il n'y a pas
            # eu de q avant, mais L[3] est True donc on n'est pas ici de toute
            # façon).
            #
            # Donc on a ici n < 2 + sqrt(N).
            #
            # Est-il possible que non seulement ce n soit composé, mais aussi
            # n + 2, n + 4, ... jusqu'à dépasser N ? Par un théorème
            # mathématique (pas évident) on sait que pour n'importe quel
            # entier n>=3 il y a un nombre premier impair p avec n <= p <=
            # 2*n. Donc il y aura parmi n + 2, n + 4, ... un premier p <= 4 +
            # 2 * sqrt(N). Alors le L[p] sera True et on arrêtera d'ajouter 2
            # bêtement.
            #
            # Mais il faut être sûr que 4 + 2 * sqrt(N) <= N
            # Un petit calcul montre que c'est le cas dès que
            #  N >= (1+sqrt(5))^2 = 10.47...
            # Donc ok pour N au moins
            # 11. Et par chance pas de problème pour N de 4 à 10.
            continue
        # ici on sait que ce n est un nombre premier
        q = N // n
        L[n::n] = [False] * q  # il y a N // n valeurs de x avec n <= n*x <= N
        L[n] = True
        if q <= n:
            # Si q <= n, alors N < (n+1)*n. Supposons qu'il y a encore un
            # entier X impair composé non criblé tel que n < X <= N. Il n'est
            # divisible par aucun entier <= n, et admet au moins deux facteurs
            # premiers, car par hypothèse il est composé, il est donc au moins
            # (n+2)**2 (car les facteurs premiers sont impairs) mais ceci est
            # > N, contradiction. En fait, contradiction déjà sous l'hypothèse
            # plus faible q <= n + 3 (car alors N < (n+4)*n < (n+2)**2).
            break
    return [n for n in range(N + 1) if L[n]]


def est_premier1(n):
    """Prédicat qui renvoie True si n est premier.

    L'implémentation doit utiliser eratosthene(n).

    :param int n: un entier à tester
    :return: True si n est premier, False sinon
    :rtype: bool
    :CU: n est positif ou nul.

    >>> est_premier1(1)
    False
    >>> est_premier1(2)
    True
    >>> est_premier1(20)
    False
    >>> est_premier1(21)
    False
    >>> est_premier1(23)
    True
    >>> est_premier1(49)
    False
    >>> est_premier1(9929)
    True
    >>> est_premier1(9927)
    False
    """
    if n <= 1:
        return False
    return n == eratosthene(n)[-1]


def plus_petit_diviseur(n):
    """Le plus petit diviseur > 1 de n

    :param int n: un entier dont on cherche le plus petit diviseur >1
    :return: le plus petit diviseur que n, autre que 1
    :rtype: int
    :CU: n est au moins 2.

    Exemples :

    >>> plus_petit_diviseur(2)
    2
    >>> plus_petit_diviseur(20)
    2
    >>> plus_petit_diviseur(21)
    3
    >>> plus_petit_diviseur(23)
    23
    >>> plus_petit_diviseur(47)
    47
    >>> plus_petit_diviseur(49)
    7
    >>> plus_petit_diviseur(9929)
    9929
    >>> plus_petit_diviseur(9927)
    3
    """
    if n % 2 == 0:  # serait plus rapide de tester n & 1
        return 2
    # dorénavant n est impair
    p = 1
    while True:
        p += 2
        q, r = divmod(n, p)
        if r == 0:
            return p
        # si on arrive ici, c'est qu'on n'a trouvé
        # aucun diviseur x impair de n avec x <= p
        # donc si n n'est pas premier il est au moins (p+2)**2 = p**2 +4*p + 4
        # donc le quotient q de n par p est au moins p + 4
        # par conséquent si q < p +4, en particulier si q <= p
        # (pas la peine de faire un +4 dans tous les tests... même si on va
        #  un peu plus loin en ne testant que q<=p)
        # alors on est sûr qu'en fait n était premier, inutile de continuer
        # à chercher un diviseur
        if q <= p:
            return n


def est_premier2(n):
    """Prédicat qui renvoie True si n est premier et False sinon

    L'implémentation doit utiliser plus_petit_diviseur(n).

    :param int n: un entier
    :return: True si n est premier, False sinon
    :rtype: bool
    :CU: n est positif ou nul

    Exemples :

    >>> est_premier2(1)
    False
    >>> est_premier2(2)
    True
    >>> est_premier2(20)
    False
    >>> est_premier2(21)
    False
    >>> est_premier2(23)
    True
    >>> est_premier2(49)
    False
    >>> est_premier2(9929)
    True
    >>> est_premier2(9927)
    False
    """
    if n <= 1:
        return False
    return n == plus_petit_diviseur(n)


def compare_premier1_et_premier2(n, reps=10000):
    """Compare (en utilisant le module timeit) est_premier1() et est_premier2()

    Pas de doctest ici, on vous demande d'implémenter la procédure suivant
    la description ci-dessous et un valeur de retour du type

    'est_premier1 est 63.64 fois plus lent que est_premier2'

    en utilisant 03.2f comme format pour le float.

    Testez-le avec n = 9929.

    :param int n: un entier au moins égal à 2.
    :return: une phrase donnant le ratio
             « durée de calcul pour est_premier1(n) » divisé
             par « durée de calcul pour est_premier(n) »
    :rtype: str
    """
    def foo1():
        return est_premier1(n)

    def foo2():
        return est_premier2(n)

    t1 = timeit.timeit(foo1, number=reps)
    t2 = timeit.timeit(foo2, number=reps)
    return "est_premier1 est %03.2f fois plus lent que est_premier2" % (t1/t2)


def factorise(n):
    """Le factorisation de n en produit de puissances de nombres premiers

    L'implémentation (pour n>=2) utilisera la procédure plus_petit_diviseur().
    En effet sa valeur de retour est automatiquement un nombre premier.

    :param int n: l'entier à factoriser
    :return: une liste de couples (p, e), avec p premier, e entier strictement
             positif, n égal au produit de tous les p**e, les p en ordre
             croissant
    :rtype: list
    :CU: n est strictement positif.

    >>> factorise(1)
    []
    >>> factorise(2)
    [(2, 1)]
    >>> factorise(4)
    [(2, 2)]
    >>> factorise(12)
    [(2, 2), (3, 1)]
    >>> factorise(100)
    [(2, 2), (5, 2)]
    >>> factorise(504)
    [(2, 3), (3, 2), (7, 1)]
    >>> factorise(539)
    [(7, 2), (11, 1)]
    >>> factorise(1024 * 13**3 * 17**2 * 19)
    [(2, 10), (13, 3), (17, 2), (19, 1)]

    """
    L = []
    while n > 1:
        p = plus_petit_diviseur(n)
        n = n // p
        a = 1
        q, r = divmod(n, p)
        while r == 0:
            a += 1
            n = q
            q, r = divmod(n, p)
        L.append((p, a))
    return L


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
