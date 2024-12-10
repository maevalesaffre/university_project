#Lesaffre Maeva
#41801943
#SESI12
from materiel_41801943 import *

##2 preliminaires
#q1 n=p*q,(e,phi(n))=1 et d*e congru à 1 modulo phi(n)

#q2 chiffrement du message, m(message clair), c(message chiffré),
# E(m), c congru à m (mod n)
# D(c), m congru à c (mod n)

#q3

#q4
#E(m),2**4240301674959461756686198219%781756346250662498153407003213
#c=24240301674959461756686198219

#D(c1),355314541288280100582449594889**4003052279448880810476873571%781756346250662498153407003213
#m1=321009951148018452028880602660

#q5
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

def congruence_est_inversible(a, N):
    """
    Prédicat disant si a est inversible modulo N

    >>> congruence_est_inversible(2, 10)
    False
    >>> congruence_est_inversible(3, 10)
    True
    >>> congruence_est_inversible(13, 26)
    False
    """
    return pgcd(a, N) == 1
#>>> congruence_est_inversible(751926387464745898426971028332, 909188195117762038410934543549)
#False, c2 n'est pas inversible modulo n2

#q6

#q7
# si m est non inversible modulo n, le problème perd l'unicité de la solution, et son existence pour tout texte chiffré,
# il est donc impossible de remonter au message initial. Le chiffrement n’est plus injectif.


#q14
#>>> congruence_est_inversible(41801943,594416529877552181020267612961)
#True, mon nip est bien inversible modulo n3
#et c3'= (((41801943**542441797998499478356836472469)%594416529877552181020267612961)*271951847996471299948737157969)%594416529877552181020267612961
#c3'=578297850808860456092934155406


