#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`lexique` module

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: janvier 2015
:last revision: février 2017

"""

with  open('lexique.txt', 'r', encoding='utf8') as f:
    mots = f.readlines()


# mise en minuscules et
# suppression du marqueur de fin de ligne pour chacun des mots
LEXIQUE = [m.lower().rstrip('\n') for m in mots]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
