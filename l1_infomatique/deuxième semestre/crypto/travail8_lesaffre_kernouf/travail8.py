#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
:auteur 1:
:auteur 2:
:groupe: SESI 12
:date: mardi 20 mars 2020
:objet: Travail numéro 8 (machine Enigma)
"""

from enigma.machine import EnigmaMachine
from cryptogrammes_enigma import CRYPTOGRAMMES
from alphabet import ALPHABETS


ALPHABET = ALPHABETS['CAPITAL_LATIN']


def nb_occurrences(txt):
    '''
    :param str txt: un texte
    :return: un dictionnaire dont les clés sont les lettres de ALPHABET
             et les valeurs associées le nombre d'occurrences de ces
             lettres dans txt.
    :rtype: dict
    :CU: txt ne doit contenir que des lettres de ALPHABET.
    
    >>> occ =  nb_occurrences('ALPHABET')
    >>> [occ[k] for k in 'ABC']
    [2, 1, 0]
    '''
    d = dict()
    for c in txt:
        if c in d:
            d[c] +=1
        else:
            d[c]=1
    print(c,':', d[c])
            
def indice_coincidences(txt):
    """
    :param str txt: un texte
    :return: l'indice de coincidence du texte txt.
    :rtype: float
    :CU: len (txt) >= 2 et tous les caractères de txt sont dans ALPHABET
    :Exemple:
    
    >>> indice_coincidences('ALPHABET') == 2 / (8*7)
    True
    """
    occ=nb_occurrences(txt)
    N=0
    somme=0
    for carac in c:
        somme += occ[c] * (occ[c] - 1)
        N += occ[c]
    return somme / (N * (N - 1)) 
        
    


def decrypte_machine_enigma_sans_fiches(chiffre):
    '''Décrypte un message chiffre d'une machine enigma sans appariements

    :param str chiffre: texte à déchiffrer
    :return: configuration probable d'une machine Enigma sans fiches
             sur le tableau de connexions
    :rtype: tuple
    :CU: cette fonction ne convient que pour des machines Enigma n'utilisant
         que les trois rotors I II et III et le réflecteur B
    '''
    # FORMAT_LIGNE = '\rOrdre rotors : {:s} Pos rotors : {:s} IC max : {:f}'
    ic_max = 0.0
    config_rotors_max = ()
    for ord_rot in ('I II III', 'I III II', 'II I III',
                    'II III I', 'III I II', 'III II I'):
        machine = EnigmaMachine.from_key_sheet(reflector='B',
                                               rotors=ord_rot,
                                               plugboard_settings='')
        print(ord_rot)
        for u in ALPHABET:
            for v in ALPHABET:
                for w in ALPHABET:
                    pos_rotors = u + v + w
                    machine.set_display(pos_rotors)
                    message = machine.process_text(chiffre)
                    ic = indice_coincidences(message)
                    if ic > ic_max:
                        config_rotors_max = (ic, ord_rot, pos_rotors)
                        ic_max = ic
                        # print('IC max = {:f} config : {} '.format(ic_max, config_rotors_max))
                    # print(FORMAT_LIGNE.format(ord_rot, pos_rotors, ic_max), end='')
    return config_rotors_max


def trouve_appariement(chiffre, rot, rotpos, appar):
    '''Détermine le nouvel appariement rendant maximal l'IC du dechiffré obtenu

    :param str chiffre: texte à déchiffrer
    :param str rot: placement des rotors
    :param str rotpos: réglage des rotors
    :param str appar: appariements déjà trouvés
    :return: l'appariement qui maximise l'indice de coincidence
    :rtype: str
    '''
    machine = EnigmaMachine.from_key_sheet(
            reflector='B',
            rotors=rot,
            plugboard_settings=appar
           )
    machine.set_display(rotpos)
    ic_max = indice_coincidences(machine.process_text(chiffre))
    app_max = ''
    for i in range(len(ALPHABET)):
        for j in range(i + 1, len(ALPHABET)):
            c1, c2 = ALPHABET[i], ALPHABET[j]
            if c1 not in appar and c2 not in appar:
                nouv_app = c1 + c2
                essai_app = appar + ' ' + nouv_app
                # print(essai_app)
                machine = EnigmaMachine.from_key_sheet(reflector='B',
                                                       rotors=rot,
                                                       plugboard_settings=essai_app)
                machine.set_display(rotpos)
                clair = machine.process_text(chiffre)
                ic = indice_coincidences(clair)
                if ic > ic_max:
                    # print(nouv_app,ic)
                    ic_max = ic
                    app_max = nouv_app
    return app_max


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
