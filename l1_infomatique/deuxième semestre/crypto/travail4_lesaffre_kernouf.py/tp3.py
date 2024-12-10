#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
:auteur 1:
:auteur 2:
:enseignant: Nicole Raulf 
:groupe: SESI 12
:date: vendredi 31 janvier 2020 
:objet: Travail numéro 3
"""


from tp1 import pgcd_étendu
from tp2 import decrypte_message
from cryptogramme_cesar import CRYPTOGRAMME
from alphabet import ALPHABETS


def solve_linear_equation(a, b, c):
    """
    :param int a, b, c: trois nombres entiers coefficients d'une
                        équation de la forme ax + by = c (1)
                        avec (a, b) pas le couple nul (0, 0)
    :return: - le tuple vide () si (1) n'a pas de solutions
             - sinon un couple de deux couples (x0, y0) et (alpha, beta)
               tels que l'ensemble des solutions de l'équation (1) soit
               l'ensemble des couples de la forme (x0 + alpha k, y0 + beta k),
               avec k un entier relatif.
    :CU: (a, b) != (0,0)

    >>> solve_linear_equation(0, 0, 1)
    Traceback (most recent call last):
    AssertionError: L'un de a ou b doit être non nul !
    >>> solve_linear_equation(4, 6, 5)
    ()
    >>> sols = solve_linear_equation(4, 6, 10)
    >>> 4 * sols[0][0] + 6 * sols[0][1]
    10
    >>> sols[1] == (-3, 2) or sols[1] == (3, -2)
    True
    >>> solve_linear_equation(121, 187, 13)
    ()
    >>> sols = solve_linear_equation(121, 187, 11)
    >>> type(sols[0][0]), type(sols[1][1])
    (<class 'int'>, <class 'int'>)
    >>> 121 * sols[0][0] + 187 * sols[0][1]
    11
    >>> sols[1] == (-17, 11) or sols[1] == (17, -11)
    True
    >>> from random import randrange
    >>> j, ok = 0, True
    >>> for i in range(100):
    ...     a, b = randrange(-999,1000), randrange(-999, 1000)
    ...     c = randrange(-9,10)
    ...     sols = solve_linear_equation(a, b, c)
    ...     if sols:
    ...         j += 1
    ...         x0, y0 = sols[0]
    ...         alpha, beta = sols[1]
    ...         ok = ok and \
                        all(a * (x0 + alpha * k) + b * (y0 + beta * k) - c == 0\
                            for k in range(-20, 20))
    ...     if not ok or j == 5:
    ...         break
    >>> ok
    True
    """
    assert (a, b) != (0, 0), "L'un de a ou b doit être non nul !"
    d, u, v = pgcd_étendu(a, b)
    if c % d != 0:
        return ()
    a1, b1, c1 = a // d, b // d, c // d
    x0, y0 = c1 * u, c1 * v
    alpha, beta = b1, -a1
    return (x0, y0), (alpha, beta)


def chiffre_lettre_affine_tp3(lettre, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """Fait le chiffrement affine de ``lettre`` par ``cle``.

    :param str lettre: lettre à chiffrer
    :param tuple cle: clé de chiffrement, un couple (a, b)
    :param Alphabet alphabet: paramètre optionnel définissant l'alphabet.
              Valeur par défaut : alphabet des 26 lettres latines capitales.
    :return: lettre chiffrée (par x -> ax + b modulo len(alphabet) au niveau
             des indices x des lettres dans l'alphabet)
    :rtype: str
    :CU: lettre doit appartenir à alphabet

    Attention, à l'avenir nous imposerons une condition supplémentaire sur la
    clé, donc cette procédure et ses doctests sont provisoires.

    >>> tuple(chiffre_lettre_affine_tp3(k, (11, 3)) for k in 'CESAR')
    ('Z', 'V', 'T', 'D', 'I')
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> tuple(chiffre_lettre_affine_tp3(k, (17, 8), decimal) for k in '012')
    ('8', '5', '2')
    >>> greek = ALPHABETS['LOWER_GREEK']
    >>> tuple(chiffre_lettre_affine_tp3(k, (11 ,3), greek) for k in 'μιακ')
    ('ω', 'ρ', 'δ', 'γ')

    """
    return alphabet[(alphabet.index(lettre) * cle[0] + cle[1]) % len(alphabet)]


def chiffre_message_affine_tp3(msg, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """Fait le chiffrement affine de ``msg`` par ``cle``.

    :param str msg: message à chiffrer
    :param tuple cle: clé de chiffrement (un couple)
    :param Alphabet alphabet: paramètre optionnel définissant l'alphabet.
              Valeur par défaut : alphabet des 26 lettres latines capitales.
    :return: message chiffré
    :rtype: str
    :CU: les caractères de ``msg`` doivent appartenir à ``alphabet``.

    Attention, à l'avenir nous vérifierons une condition supplémentaire sur la
    clé, donc cette procédure est une version provisoire.

    >>> chiffre_message_affine_tp3('CESAR', (11, 3))
    'ZVTDI'
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> chiffre_message_affine_tp3('012', (17, 8), decimal)
    '852'
    >>> greek = ALPHABETS['LOWER_GREEK']
    >>> chiffre_message_affine_tp3('μιακ', (11, 3), greek)
    'ωρδγ'
    """
    return ''.join(chiffre_lettre_affine_tp3(x, cle, alphabet) for x in msg)


# print(decrypte_message(CRYPTOGRAMME, ' ', ALPHABETS['PRINTABLE_ASCII'])[0].replace('@', '\n'))


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
