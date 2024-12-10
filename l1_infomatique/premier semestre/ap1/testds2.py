
#DS 2017/2018
from math import sqrt
from random import randint
from itertools import permutations
#exo 1
#q1
#b%10, ou souhaite trouver le reste de cette division euclidienne. b//10, ou souhaite trouver le quotient de cette division

#q2
"""
>>> mystere(2018)
Au début, s= 0 et b= 2018
s= 64 et b= 201
s= 65 et b= 20
s= 65 et b= 2
s= 69 et b= 0
69
"""

def mystere(a):
    s=0
    b=a
    print("Au début, s=", s, "et b=",b)
    while b>0:
        s=s+(b%10)**2
        b=b//10
        print("s=",s,"et b=",b)
    return s
        
        
#q3
#q4
#si a  est négatif ou nul, il renvoie 0

#q5
    """
    renvoie ? à revoir
    :param a: (int) un entier
    :return s: (int) un entier
    :CU: None
    
    :exemples:
    >>> mystere(-8)
    0
    """
    
#exo 2
#q1
def racine_premiere_tranche(n):
    if 1<=n<4:
        racine_n=1
    elif 4<=n<9:
        racine_n=2
    elif 9<=n<16:
        racine_n=3
    elif 16<=n<25:
        racine_n=4
    elif 25<=n<36:
        racine_n=5
    elif 36<=n<49:
        racine_n=6
    elif 49<=n<64:
        racine_n=7
    elif 64<=n<81:
        racine_n=8
    elif 81<=n<100:
        racine_n=9
    return racine_n
    
# q2
def tranche_de_droite(n):
    n1=n%100
    return n1
#q3
def autres_tranches(n):
    n1=n//100
    return n1    
#q4
def decouper(n):
    n1=autres_tranches(n)
    n2=autres_tranches(n1)
    n3=tranche_de_droite(n1)
    n4=tranche_de_droite(n)
    tu=(n2,n3,n4)
    return tu
#q5 à voir
def chiffre_suivant(p,r):
    d=0
    while (20*r+d)*d <= p:
        d+=1
    d=d-1
    return d
#q6
#voir ligne 1

#exo3
#q1
def nombreCaracteres(string):
    longueur=len(string)
    return longueur
#q2
def enleveEspaceDF(string):
    return string.strip()
#q3
def nombresMots(string):
    phrase1=enleveEspaceDF(string)
    prec, nb_mots = ' ', 0
    for char in phrase1:
        nb_mots += int(prec == ' ' and char != ' ')
        prec = char
    return nb_mots
#q5
def validationTweet(string):
    if nombreCaracteres(string)<280:
        print("Votre tweet de",nombresMots(string),"mot(s) a bien été envoyé")
    else:
        print("Votre tweet est trop long,il contient",nombreCaracteres(string))
        

        
#DS 2016-2017
#exo1
#q1 
def mystere_Un(nbr):
    interieur=0
    for i in range(0,nbr-1):
        x=randint(0,1)
        y=randint(0,1)
        if (x*x+y*y)<1:
            interieur+=1
    return (4*interieur)/nbr

#exo2
#q1
def dejaTire(n,L):
    if n in L:
        return True
    else:
        return False
#q2 à vérifier histoire de int distinct
def tirage():
    tu= tuple()
    for i in range(6):
        co= randint(0,50)
        while co in tu:
            co=randint(0,50)
        tu= tu + (co,)
    return tu

#q3
def gagant(bulletin,tirage):
    i=0
    for carac in bulletin:
        if carac in tirage:
            i+=1
    return i>=3

        
#q4



#exo4
#q1
def gagne(objet1,objet2):
    if objet1=="ciseaux" and objet2=="feuille":
        return True
    elif objet1=="feuille" and objet2=="pierre":
        return True
    elif objet1=="pierre" and objet2=="ciseaux":
        return True
    else:
        return False
        
#q2
def est_liste_correcte(tu):
    if len(tu)%2!=0:
        return False
    for carac in tu:
        if carac !="pierre" or carac != "ciseaux" or carac != "feuille":
            return False
    return True
        
    
#DS   2018-2019
#exo2   
#q1
def est_multiple(nb):
    if nb%3==0:
        return True
    else:
        return False
#q2
def somme_egale_12(tu):
    if tu[0]+tu[1]+tu[2]==12:
        return True
    else:
        return False
#q3
def genere_combinaisons():
    a=randint(0,10000)
    b=randint(0,10000)
    c=randint(0,10000)
    tu=(a,b,c)
    for carac in permutations(tu):
        print(carac)
       
#q4
"""
def affiche_combinaisons(genere_combinaisons()):
    for carac in genere_combinaisons():
        if est_multiple(carac)==True and somme_egale_12(carac)==True:
            print(carac)
"""

#exo3
#q1
def genereMinuscule():
    a1=randint(97,122)
    caractere=chr(a1)
    return caractere
        
#q2
def genereMot(n):
    mdp = "" 
    compteur = 0 
    while compteur < n:
        lettre = genereMinuscule() 
        mdp += lettre 
        compteur += 1
    return mdp
    
#q3


#q4 à revoir
def changeLettrePos(chaine,pos):
    chainefinal=chaine.replace(chaine[pos],genereMinuscule())
    return chainefinal


    
    