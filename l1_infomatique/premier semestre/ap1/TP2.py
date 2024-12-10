from datetime import *
from math import *
import doctest

#exo1 Maeva Lesaffre
#q1
#c=20


#q2
#>>> c=20
#>>> f=(9/5)*c+32
#>>> print (f)

#q3
c=20
f=(9/5)*c+32
print("Une température de", c ,"°C correspond à une température de", f)

#q4
F2= 75
C2= (5/9)*(F2-32)
print("Une température de", F2 ,"F correspond à une température de", C2)

#q5
def celsius_en_fahrenheit (C):
     """
     convertit une température en degrés Celsius
     passée en paramètre et renvoie la température
     exprimée en Fahrenheit.
     :C: (int or float) temperature en c°.
     :return : F, C° convertit en fahrenheit.
     
     CU : C!= str
     
     exemples:
     >>> (9/5)*20+32
     68.0
     """
     F=(9/5)*C+32
     return F

#q6
def fahrenheit_en_celsius (F2):
    """
    convertit une température en degrés Fahrenheit
    passée en paramètre et renvoie la température
    exprimée en Celsius.
    :F2: (int or float) temperature en F.
    :return: C2, F convertit en C°.
    
    CU : F2!= str
    
    exemples:
    >>> (5/9)*(F2-32)
    23.88888888888889
    """
    C2= (5/9)*(F2-32)
    return C2

#q7
#>>> celsius_en_fahrenheit(fahrenheit_en_celsius(20))
#20.0

#exercice 2
#q1
ref_an= 1900
ref_mois= 1
ref_jour=1
#q2
nbre_sec_jour= 60*60*24
#q3
nbre_sec_an= nbre_sec_jour*365.2425
#q4
nbre_sec_mois= nbre_sec_an/12
#q5
aujourdhui_an=2019
aujourdhui_mois=9
aujourdhui_jour=16

#q6
#>>> nbre_sec_jour= 60*60*24
#>>> nbre_sec_an= nbre_sec_jour*365.2425
#>>> nbre_sec_mois= nbre_sec_an/12
#>>> nbre_sec_jour*16+(nbre_sec_mois)*9+nbre_sec_an*119
#3780327402.0

#q7
#nbre_sec_jour= 60*60*24
#>>> nbre_sec_an= nbre_sec_jour*365.2425
#>>> nbre_sec_mois= nbre_sec_an/12
#nbre_sec_jour*19+(nbre_sec_mois)*5+nbre_sec_an*99
#3138928578.0

#q8
#>>> 3780327402.0-3138928578.0
#641398824.0

#q9
def nbre_sec_depuis_1900(jour,mois,année):
    """
    calcule le nombre approximatif de secondes écoulées
    entre la date de référence à 0h00 et celle passée en paramètre.
    :jour: (int) jour de la date.
    :mois: (int) mois de la date.
    :année: (int) année de la date.
    :return: toto le nombre approximatif de secondes écoulées
    entre la date de référence à 0h00 et celle passée en paramètre.
    
    CU: jour,mois,année!=str
    
    exemples:
    >>> nbre_sec_depuis_1900(19,5,1999)
    3138928578.0
    
    """
    nbre_sec_jour= 60*60*24
    nbre_sec_an= nbre_sec_jour*365.2425
    nbre_sec_mois= nbre_sec_an/12
    toto=nbre_sec_jour*jour+(nbre_sec_mois)*mois+nbre_sec_an*(année-1900)
    return toto

#q10
#>>> nbre_sec_depuis_1900(19,5,1999)
#3138928578.0
#>>> 3780327402.0-3138928578.0
#641398824.0

#q11
#aujourdhui = date.today()
#jouractuel=aujourdhui.day
#moisactuel=aujourdhui.month
#annéeactuel=aujourdhui.year

#fin=nbre_sec_depuis_1900(jouractuel,moisactuel,annéeactuel)
#anniv=fin-641398824.0
#print(anniv)

#q12
def age_en_secondes(journaissance,moisnaissance,annéesnaissance):
    """
    calcule l’âge en secondes d’une personne dont on donne la date de naissance en paramètre.
    :journaissance: (int) jour de la date de naissance.
    :mois: (int) mois de la date de naissance.
    :année: (int) année de la date de naissance.
    :return: toto le nombre approximatif de l'âge en secondes, grâce à la date passée en paramètre.
    
    CU: jourdenaissance,moisdenaissance,annéedenaissance !=str
    
    exemples:
    >>> age_en_secondes(19,5,1999)
    641744424.0
    """
    nbre_sec_jour= 60*60*24
    nbre_sec_an= nbre_sec_jour*365.2425
    nbre_sec_mois= nbre_sec_an/12
    aujourdhui = date.today()
    jouractuel=aujourdhui.day
    moisactuel=aujourdhui.month
    annéeactuel=aujourdhui.year
    toto=nbre_sec_jour*(jouractuel-journaissance)+nbre_sec_mois*(moisactuel-moisnaissance)+nbre_sec_an*(annéeactuel-annéesnaissance)
    return toto


#exercice 3
#q1 et q2
def undefined(x):
    """
    compte le nombre de caractères d'entiers passés en paramètre.
    :x: (int or float) l'entier ou le nombre flottant.
    :return: b le nombre de caractères d'entiers.
    
    CU: x!=str
    >>> undefined(1.5)
    1
    >>> undefined(13)
    2
    """
    a = log10(x) + 1
    b = floor(a)
    return b

#help(undefined)
#Help on function undefined in module __main__:

#undefined(x)
#    compte le nombre de caractères d'entiers passés en paramètre.
#    :x: (int or float) l'entier ou le nombre flottant.
#    :return: b le nombre de caractères d'entiers.
    
#    CU: x!=str
#    >>> undefined(1.5)
#    1
#    >>> undefined(13)
#    2

doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)