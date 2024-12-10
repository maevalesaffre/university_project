#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
:étudiant 1: Lesaffre maeva
:étudiant 2: Kernouf sabrina
:groupe: SESI 12 
:date: vendredi 21 février 2020 
:objet: Travail numéro 6 (cryptographie)

Lisez attentivement la docstring du fichier cryptogrammes_vigenere.py.

Il s'agit donc :

- de retrouver chaque clé (tuple d'entiers) en découvrant les prénoms
  qu'elles chiffrent,

- une fois ces clés trouvées, il ne reste plus qu'à déchiffrer les message
  correspondants. Il vous faut deviner les alphabets utilisés parmi ceux du
  module alphabet.py.

Je rappelle que vous avez déjà codé en TP4 la procédure de déchiffrement.

Indiquez ci-dessous les étapes suivies.
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
