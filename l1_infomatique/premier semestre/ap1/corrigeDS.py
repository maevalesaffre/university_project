# Lesaffre Maeva, Mélanie Bulois DS N°1
from math import log
from random import randint
import doctest
 
## Exercice 1
### Question 1 : Modulo
n = 121231446673253135466736253
#### print( n % 7 ) donne True.
 
### Question 2 : Chaînes
#### print("999" == 3 * "9") donne True.
 
### Question 3 : Chaînes, le retour.
#### print("5", "+", "7") donne "5 + 7".
 
### Question 4 : Soustraction
#### print(-11---11) donne -22.
 
### Question 5 : Affectation de variables
x = 1
y = 2
z = y
y = x
x = z
#### print(x, y, z) donne 2 1 2.
 
### Question 6 : Conditions
z = 0
#### print( z < 0 or z != 1) donne True.
 
### Question 7 : Longueur de chaînes
### print(len("Info") >= len("Math" - "Chimie")) donne une erreur, puisqu'il n'y existe pas de soutraction de chaînes.
 
### Question 8  : Plus grand que
u = 13 > 14
#### print(u or not u) donne True
 
### Question 9 : Conditions 2
test = 0
if test >= 0:
    test = test - 2
if test < 0:
    test = test + 3
#### print(test) donne 1.
   
### Question 10 : Variables
a = 2
b = 2
#### print((a + b) ** 2) donne 16.
 
## Exercice 2
### Question 1
#### On doit utiliser 'from math import log' au début du code pour pouvoir l'utiliser.
 
### Question 2
#### La fonction round(f, n) calcule l'arrondi d'un décimal en fonction du nombre après la virgule passé en paramètre.
 
### Question 3 : alpha(t, h)
def alpha(t, h):
    """
    Renvoie alpha(t, h), une formule utilisé pour calculer le point de rosée en thermodynamique.
    :param t: (float) Une température en degré celsius.
    :param h: (float) Une humidité relative
    :CU: 0°C < t < 60°C, 0,01 < h < 1
 
    Exemples :
    >>> alpha(50, 0.5)
    2.308243156596815
    >>> alpha(60, 0.01)
    -1.1244849323770727
    """
    a = 17.27
    b = 237.7
    return ((a * t) / (b + t)) + log(h)
 
### Question 4 : point_rosee(t, h)
def point_rosee(t, h):
    """
    Renvoie le point de rosée aproximatif avec une précision de 2 décimales.
    :param t: (float) Une température en degré celsius.
    :param h: (float) Une humidité relative
    :CU: 0°C < t < 60°C, 0,01 < h < 1
   
    Exemples :
    >>> point_rosee(50, 0.5)
    36.67
   
    >>> point_rosee(60, 0.01)
    -14.53
    """
    a = 17.27
    b = 237.7
    rep = ((b * alpha(t,h)) / (a - alpha(t, h)))
    return round(rep, 2)
   
### Question 5
def au_hasard():
    t = randint(20, 30)
    h = (randint(50, 70) / 100)
    print('Le point de rosée pour t =', t, 'et h =', h,'% vaut', point_rosee(t, h),'°C.')
 
### Question 6
def mesures_coherentes(p, t):
    if (5.5 <= p <= 10.5) and (20 <= t <= 25):
        return True
    elif (10.4 <= p <=15) and (25 <= t <= 30):
        return True
    else:
        return False
 
### Question 7
def note(p1, p2, p3, t1, t2, t3):
    note = 0
    if mesures_coherentes(p1, t1):
        note = 1
        if mesures_coherentes(p2, t2):
            note = 3
            if mesures_coherentes(p3, t3):
                note = 5
    return note
 
# Exercice 3
def en_dot_beat(h, m, s):
    """
    Retourne un temps en heure, minutes, et secondes passés en paramètres en battements de temps internet.
    :param h: (int) Une heure.
    :param m: (int) Une minute.
    :param s: (float) Une seconde.
    :CU: 0 <= h <= 23, 0 <= m <= 59, 0.0 <= s <= 60.0
   
    Exemples :
    >>> en_dot_beat(1, 1, 1)
    129.50666666666666
   
    >>> en_dot_beat(10, 1, 1)
    504.50666666666666
    """
    beat = 0
    beat += h / 0.024 + m * 1.44 + s * 86.4
    return beat
 
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)