# Lesaffre Maeva Kernouf Sabrina
# le 06/02/19


## Import
from timeit import timeit
from lexique import LEXIQUE
import doctest
s= "la méthode split est parfois bien utile"

##        Methode split        ##
"""
>>> s.split('')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: empty separator
>>> s.split('e')
['la méthod', ' split ', 'st parfois bi', 'n util', '']
>>> s.split('é')
['la m', 'thode split est parfois bien utile']
>>> s.split()
['la', 'méthode', 'split', 'est', 'parfois', 'bien', 'utile']
>>> s.plit(' ')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'str' object has no attribute 'plit'
>>> s.split('split')
['la méthode ', ' est parfois bien utile']
"""
l=s.split()




##        Methode join        ##
"""
1)
>>>"".join(1))
TypeError: can only join an iterable
>>> " ".join(l)
'la méthode split est parfois bien utile'
>>> ";".join(l)
'la;méthode;split;est;parfois;bien;utile'
>>> " tralala ".join(l)
'la tralala méthode tralala split tralala est tralala parfois tralala bien tralala utile'
>>> print ("\n".join(l))
la
méthode
split
est
parfois
bien
utile
>>> "".join(s)
'la méthode split est parfois bien utile'
>>> "!".join(s)
'l!a! !m!é!t!h!o!d!e! !s!p!l!i!t! !e!s!t! !p!a!r!f!o!i!s! !b!i!e!n! !u!t!i!l!e'
>>> "".join()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: join() takes exactly one argument (0 given)
>>> "".join([])
''
>>> "".join([1,2])
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found

2)join intercale la chaîne de caractère devant entre chaque éléments
de la liste entré entre les parenthèse et rassemble le tout

3) la methode ne change pas la chaine de caractère a laquelle elle s'applique
"""


def join(s,l):
    """
    renvoie une chaîne de caractères construite en concaténant toutes les chaînes de l en intercalant s sans utiliser la méthode homonyme
    :param msg: (str) chaîne de caractères
    :param l: (list) liste de chaînes de caractères
    :CU: None
    :Example:
    >>> join('.', ['raymond', 'calbuth', 'ronchin', 'fr'])
    'raymond.calbuth.ronchin.fr'
    """
    msg = ""
    for element in l:
        if element == l[len(l)-1]:
            msg += element
        else:
            msg += element+s
    return msg
##        Methode sort        ##
"""
>>> l=list('timoleon')
>>> l.sort()
>>> l
['e', 'i', 'l', 'm', 'n', 'o', 'o', 't']
>>> s = "Je n'ai jamais joué de flûte"
>>> l = list(s)
>>> l.sort()
>>> l
[' ', ' ', ' ', ' ', ' ', "'", 'J', 'a', 'a', 'a', 'd', 'e', 'e', 'e', 'f', 'i', 'i', 'j', 'j', 'l', 'm', 'n', 'o', 's', 't', 'u', 'é', 'û']


1) Les caractères sont rangé dans l'ordre croissant du code ascii.
2)

>>> l = ["a",1]
>>> l.sort()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'

On ne peut pas comparer deux element qui ne sont pas du même type
"""



##   une fonction sort pour les chaines

def sort(s):
    """
    trie la chaine de caractère entrée en parametre par ordre lexicographique.
    :param s: (str) une chaine de caratcères
    :return: (str)
    :CU: none
    :Exemple:
    >>> sort('timoleon')
    'eilmnoot'
    """
    s = list(s)
    s.sort()
    st = ""
    for lettre in s:
        st+=lettre
    return st
    
##   Anagrammes    ##

#q1
def sont_anagrammes_v1(s1, s2):
    """
    renvoie le booléen True si ces deux chaînes sont anagrammatiques, et le booléen False dans le cas contraire.
    :param s1: (str) une chaine de caractères
    :param s2: (str) une chaine de caractères
    :return:(bool) - True si s1 et s2 sont anagrammatiques - False sinon
    :CU: none
    :Exemple:
    >>> sont_anagrammes_v1('orange', 'organe')
    True
    """
    s1= sort(s1)
    s2=sort(s2)
    n= 0
    if len(s1) != len(s2):
        return False
    for lettre in s1:
        if lettre != s2[n]:
            return False
        n+=1
    return True
    
#q2
def nb_occ(msg):
    """
    renvoie dans un dictionaire le nombre d'occurence de chaque lettre dans un message
    :parama msg: (str) le message dans le quel on veut calculer le nombre de caractere
    :return: (dict) le dictionaire des lettres avec en valeur leur nombre d'occurence
    :CU: none
    """
    nb_occ=dict()
    for carac in msg:
        if carac in nb_occ:
            nb_occ[carac]+=1
        else:
            nb_occ[carac]=1
    return nb_occ


def sont_anagrammes_v2(s1, s2):
    """
    renvoie le booléen True si ces deux chaînes sont anagrammatiques, et le booléen False dans le cas contraire.
    :param s1: (str) une chaine de caractères
    :param s2: (str) une chaine de caractères
    :return:(bool) - True si s1 et s2 sont anagrammatiques - False sinon
    :CU: none
    :Exemple:
    >>> sont_anagrammes_v2('orange', 'organe')
    True
    """
    s1=nb_occ(s1)
    s2=nb_occ(s2)
    if len(s1)!=len(s2):
        return False
    for carac in s1:
        if s1[carac]!=s2[carac]:
            return False
    return True


#q3        
def sont_anagrammes_v3(s1, s2):
    """
    renvoie le booléen True si ces deux chaînes sont anagrammatiques, et le booléen False dans le cas contraire.
    :param s1: (str) une chaine de caractères
    :param s2: (str) une chaine de caractères
    :return:(bool) - True si s1 et s2 sont anagrammatiques - False sinon
    :CU: none
    :Exemple:
    >>> sont_anagrammes_v3('orange', 'organe')
    True
    """
    if len(s1)!=len(s2):
        return False
    for carac in s1:
        if s1.count(carac) != s2.count(carac):
            return False
    return True

# dictionaire de l'equivalence de chaque caractere spéciaux en lettre simple
#q1
EQUIV_NON_ACCENTUE ={'à':"a", 'ã':"a", 'á':"a", 'â':"a",
                    'é':'e', 'è':'e', 'ê':'e', 'ë':'e',
                    'î':'i', 'ï':'i',
                    'ù':'u', 'ü':'u', 'û':'u',
                    'ô':"o", 'ö':"o",
                    "ç":"c"}

##   Casse et accentuation
def bas_casse_sans_accent(s):
    """
    prédicat qui ne différencie pas les lettres selon leur casse ou leur accentuation.
    :param s: (str) une chaine de caractères
    :return msg: (list) renvoie la liste sans leur accentuation ou leur casse.
    :CU: none
    :Exemple:
    >>> bas_casse_sans_accent('Orangé')
    'orange'
    """
    msg=""
    for carac in s:
        if carac in EQUIV_NON_ACCENTUE:
            carac=EQUIV_NON_ACCENTUE[carac]
        msg+=carac
        msg=msg.lower()
    return msg
        
        
def sont_anagrammes_v4(s1,s2):
    """
    renvoie le booléen True si ces deux chaînes sont anagrammatiques, et le booléen False dans le cas contraire.
    :param s1: (str) une chaine de caractères
    :param s2: (str) une chaine de caractères
    :return:(bool) - True si s1 et s2 sont anagrammatiques - False sinon
    :CU: none
    :Exemple:
    >>> sont_anagrammes_v4('orange', 'organe')
    True
    >>> sont_anagrammes_v4('orange','Organe')
    True
    """
    if len(s1)!=len(s2):
        return False
    s1=bas_casse_sans_accent(s1)
    s2=bas_casse_sans_accent(s2)
    for carac in s1:
        if s1.count(carac) != s2.count(carac):
            return False
    return True

##   Recherche d'anagrammes

# le lexique        
    
#>>> len(LEXIQUE)
#139719    


#>>> s = len(set(LEXIQUE))
#>>> l = len(LEXIQUE)
#>>> s == l
#True
#donc pas de doublons



# Anagrammes d’un mot : première méthode

def anagrammes_v1(mot):
    """
    renvoie la liste des anagrammes d’un mot passé en paramètre, ces anagrammes appartenant au lexique
    :param mot: (str) un mot dont on veut les anagrammes.
    :return:(list) la liste des mots figurant dans le LEXIQUE qui sont des anagrammes de mot.
    :CU: none
    :Exemple:
    >>> anagrammes_v1('orange')
    ['onagre', 'orange', 'orangé', 'organe', 'rongea']
    >>> anagrammes_v1('info')
    ['foin']
    >>> anagrammes_v1('Calbuth')
    []
    >>> anagrames_v1("chien")
    ['chien', 'chiné', 'niche', 'niché']
    """
    
    listee=[]
    for carac in LEXIQUE:
        if sont_anagrammes_v4(carac,mot)== True:
            listee=listee + [carac,]
    return listee

#q2
#>>> anagrammes("chien")
#['chien', 'chiné', 'niche', 'niché']

# anagrammes d'un mot, seconde méthode

# creation des cles de dictionaire
def cle(mot):
    """
    renvoie la cle du mot entrer en parametre pour le dictionaire d'anagrammes, qui est le mot en minuscule et les lettres rangés dans l'ordre alphabetique.
    :param mot: (str) un mot dont on veut la cle.
    :return:(str) le mot en minuscule et les lettres rangé dans l'ordre alphabetique.
    :CU: none
    :Example:
    >>> cle('Orangé')
    'aegnor'
    """
    mot1=bas_casse_sans_accent(mot)
    mot1=sort(mot1)
    return mot1

# definition du dictionaire d'anagrammes
d = {}
for mot in LEXIQUE:
    if cle(mot) in d:
        d[cle(mot)].append(mot)
    else:
        d[cle(mot)] = [mot]
ANAGRAMMES = d


def anagrammes_v2(mot):
    """
    renvoie la liste des anagrammes d’un mot passé en paramètre, ces anagrammes appartenant au lexique
    :param mot: (str) un mot dont on veut les anagrammes.
    :return:(list) la liste des mots figurant dans le LEXIQUE qui sont des anagrammes de mot.
    :CU: none
    :Exemple:
    >>> anagrammes_v2('orange')
    ['onagre', 'orange', 'orangé', 'organe', 'rongea']
    >>> anagrammes_v2('info')
    ['foin']
    >>> anagrammes_v2('Calbuth')
    []
    >>> anagrammes_v2("chien")
    ['chien', 'chiné', 'niche', 'niché']
    """
    cl = cle(mot)
    if cl in ANAGRAMMES:
        ana = ANAGRAMMES[cl]
    else:
        ana = []
    return ana

#>>> anagrammes_v2("chien")
#['chien', 'chiné', 'niche', 'niché']

##   Comparaison des deux méthodes

court = LEXIQUE[:30]


#temps pris par la version 1 de la fonction anagrammes pour 10 repetition
# 1.594437347000003 s
for word in court:
   t1 = timeit(stmt='anagrammes_v1(word)',
           setup='from __main__ import anagrammes_v1, word',
           number = 10)
print(t1)


#temps pris par la version 2 de la fonction anagrammes pour 10 repetition
# 5.087200000275516e-05 s
for mot in court:
   t2 = timeit(stmt='anagrammes_v2(mot)',
           setup='from __main__ import anagrammes_v2, mot',
           number = 10)
print(t2)

# On remarque La deuxieme version  de anagramme est beaucoup plus rapide que la version 1


#doctest
"""
if __name__ == '__main__':
     import doctest
     doctest.testmod (optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)
     """