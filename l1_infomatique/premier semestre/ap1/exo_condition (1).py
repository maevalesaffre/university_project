#lesaffre maeva, Rémi Sourdaine
#TP 4 exercice sur les conditions

from random import randint
import doctest

#Exercice 1
#Q1
def est_dans1(x):
    """
    fonction renvoyant True si x appartient à l'intervalle [−1;3] et False sinon.
    :param x: (float)  
    :return: (booléen)True ou False
    :CU: None
    
    :exemples:
    >>> est_dans1(1)
    True
    >>> est_dans1(6)
    False
    """
    
    return -1<=x and x <=3

def est_dans2(x):
    """
    fonction renvoyant True si x appartient à l'intervalle ]−1;3] et False sinon.
    :param x: (float)  
    :return: (bool) retourne True ou False 
    :CU: None
    
    :exemples:
    >>> est_dans2(1)
    True
    >>> est_dans2(-1)
    False
    """
    
    return -1<x and x <=3

def est_dans3(x):
    """
    fonction renvoyant True si x appartient à l'intervalle ]−1;3]ou[8;10[ et False sinon.
    :param x: (float)  
    :return: (bool)True ou False
    :CU:None
    
    :exemples:
    >>> est_dans3(8)
    True
    >>> est_dans3(5)
    False
    """
    return (-1<x and x <=3) or (8<=x and x<10 )

def est_dans4(x):
    """
    fonction renvoyant True si x appartient à l'intervalle ]−1;3]ou[8;+∞[ et False sinon.
    :param x: (float)  
    :return: (bool)True ou False
    :CU:aucun
    
    :exemples:
    >>> est_dans4(100)
    True
    >>> est_dans4(-100)
    False
    """
    return (-1<x and x <=3) or (8<=x )

#Q2
def est_positif(nb):
    """
    prédicat renvoyant True si le nombre passé en paramètre est positif ou nul, et False s'il est strictement négatif.
    :param nb: (int) un entier
    :return: (booléen) True ou False
    :CU: None
    
    :exemples:
    >>> est_positif(1)
    True
    >>> est_positif(-2)
    False
    """
    return nb>=0

def meme_signe(nb1,nb2):
    """
    prédicat meme_signe renvoyant True si les deux nombres passés en paramètre sont soit
    tous les deux positifs ou nuls, soit tous les deux négatifs ou nuls, et False sinon
    :param nb1: (int) un entier
    :param nb2: (int) un entier
    :return: (booléen) True ou False
    :CU: None
    
    :exemples:
    >>> meme_signe(1,2)
    True
    >>> meme_signe(-12,6)
    False
    """
    return (nb1>=0 and nb2>=0) or (nb1<=0 and nb2<=0)

#Q3
def dans_rectangle(x,y):
    """
    Définissez un prédicat paramétré par deux nombres représentant l'abscisse et l'ordonnée d'un
    point M et renvoyant True si M est dans le rectangle rouge et False sinon.
    :param x: axe des abscisses
    :param y: axe des ordonnées
    :return: (booléen) True ou False
    :CU: None
    
    exemples:
    >>> dans_rectangle(5,6)
    True
    >>> dans_rectangle(1,10)
    False
    """
    return (x>=2 and x<=10) and (y>=4 and y<=8)

def dans_disque(x,y):
    """
    Définissez un prédicat paramétré par deux nombres représentant l'abscisse et l'ordonnée d'un point M et
    renvoyant True si M est dans le disque rouge dont le centre a pour coordonnées (6,4) et dont le rayon est 2 ;
    et False sinon.
    :param x: (int)axe des absisses
    :param y: (int)axe des ordonnées
    :return: (booléen) True ou False
    :CU: None
    
    exemples:
    >>> dans_disque(7,3)
    True
    >>> dans_disque(8,3)
    False
    """
    return (x-6)**2 +(y-4)**2 <= 4 #4 correspond au diamètre
    
#Q4 
def est_pair(nb):
    """
    prédicat renvoyant True si l'entier passé en paramètre est pair, et False sinon.
    :param nb: (int) un entier
    :return: (booléen) True ou False
    :CU: None
    
    exemples:
    >>> est_pair(4)
    True
    >>> est_pair(5)
    False
    """
    return nb%2 == 0

def yacoupe(nb):
    """
    prédicat renvoyant True si l'entier passé en paramètre est une année de coupe du monde et False sinon.
    :param nb: (int) un entier
    :return: (bool) True ou False
    :CU: année supérieur a 1930, année paire, année non multiple de 4
    
    exemples:
    >>> yacoupe(1945)
    False
    >>> yacoupe(1934)
    True
    """
    return (nb>=1930 and nb<1942 or nb>1946 ) and (nb-1930)%4 == 0


#Exercise 2
#Q1
def  maximum(a,b):
    """
    fonction prenant en paramètre 2 nombres et renvoyant le maximum de ces deux nombres.
    :param a: (int) premier entier
    :param b: (int) deuxieme entier
    :return: le plus grand nombre des deux
    :CU: None
    
    exemples:
    >>> maximum(2,7)
    7
    >>> maximum(9,7)
    9
    """
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return a

def minimum(a,b):
    """
    fonction prenant en paramètre 2 nombres et renvoyant le minimum de ces deux nombres.
    :param a: (int)premier entier
    :param b: (int)deuxieme entier
    :return: le plus petit nombre des deux
    :CU: None
    
    :exemples:
    >>> minimum(2,7)
    2
    >>> minimum(9,7)
    7
    """
    if a<b:
        return a
    elif b<a:
        return b
    else:
        return a

def valeur_absolue(a):
    """
    fonction prenant en paramètre 1 nombre et renvoyant la valeur absolue de ce nombre.
    :param a: (int)entier relatif
    :return: entier sous sa valeur absolue
    :CU: None
    
    :exemples:
    >>> valeur_absolue(4)
    4
    >>> valeur_absolue(-15)
    15
    """
    if a>=0:
        return a
    else:
        return -a
    
def pile_ou_face():
    """
    renvoie aleatoirement 'pile' ou 'face'
    :return: (str) pile ou face
    :CU: None

    """
    p = randint(0,1)
    if p == 0:
        return "face"
    else:
        return "pile"
    
#Exercise 3
def cle(groupe):
    gp = input('Entrez votre clé de groupe: ')
    if gp == "info_17-18_"+str(groupe):
        print("Bienvenue dans le groupe",gp, "!")
    else:
        print("Mot de passe invalide!")

#Exercise 4
def est_rectangle(a,b,c,error):
    """
    prédicat est_rectangle paramétré par 4 flottants, les trois premiers représentant les
    longueurs des côtés d'un triangle et le dernier l'erreur acceptable, et renvoyant True
    si le triangle est rectangle, et False sinon.
    :param a: (int) premier entier
    :param b: (int) deuxieme entier
    :param c: (int) troisieme entier
    :param error: (int) erreur acceptable
    :return: (booléen) True ou False
    :CU: Soit error un entier strictement positif représentant l'erreur absolue acceptable
    
    exemples:
    >>> est_rectangle(2,3,4,5)
    False
    >>> est_rectangle(3,4,5,3)
    True
    >>> est_rectangle(3,4,5,0)
    True
    """
    return (c**2 == a**2+b**2 or a**2 == c**2+b**2 or b**2 == a**2+c**2) and ( (a**2 +b**2- error <= c**2 and a**2 +b**2- error <= c**2) or (c**2 +b**2- error <= a**2 and c**2 +b**2- error <= a**2) or (c**2 +a**2- error <= b**2 and c**2 +a**2- error <= b**2)  )
    
#Exercise 5
def est_perime(d,m,y,de,me,ye):
    """
    prédicat est_perime prenant en paramètres 6 entiers : les trois premiers représentant la date du jour et les
    trois derniers la date de péremption d'un produit. Ce prédicat doit renvoyer True si la date du jour est postérieure
    à la date de péremption et False sinon.
    :param d: (int) premier entier
    :param m: (int) deuxieme entier
    :param y: (int) troixieme entier
    :param de: (int) quatrieme entier
    :param me: (int) cinquieme entier
    :param ye: (int) sixieme entier
    :return: (booléen) True ou False
    :CU: None
    
    exemples:
    >>> est_perime(4,5,18,3,5,18)
    True
    >>> est_perime(4,5,18,4,7,18)
    False
    """
    return y>ye or  ( y == ye and m>me )or ( y == ye and m == me and d>=de)

doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)

