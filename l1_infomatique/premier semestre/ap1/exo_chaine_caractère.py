#LESAFFRE maeva
# SELEMANI faida
#exo chaîne de caractère
import doctest
#exercice1
#print("\n \n \n \n")

#exercice2
def imprimer_vertical(str):
    """
    imprime un à un les caractères de la chaîne qu’on
    lui donne en paramètre les uns au dessous des autres.
    :param str: (str) chaîne de caractère.
    :print carac: (str) une chaine de caractère affiché les uns au dessous des autres.
    :CU: None
    
    exemples:
    >>> imprimer_vertical("potatoes")
    p
    o
    t
    a
    t
    o
    e
    s
    """
    for carac in str:
        print(carac)
        
#exercice 3
def my_len(str):
    """
    renvoie la longueur de la chaîne de caractères
    qu’on lui passe en paramètre.
    :param str: (str) chaine de caractère.
    :return x:(int) longueur de la chaîne de caractères.
    :CU: None
    
    exemples:
    >>> my_len('')
    0
    >>> my_len('abcd')
    4 
    """
    x=0
    for carac in str:
        x+=1
    return x

#exercice 4
#q1
def tirets(str):
    """
    renvoie une chaîne construite à partir de celle reçue en paramètre en
    insérant un tiret derrière chacun de ses caractères.
    :param str:(str) chaîne de caractères.
    :return x:(str) chaîne de caractères avec un tiret derrière chacun de
    ses caractères.
    :CU: None
    
    exemples:
    >>> tirets('Timoleon')
    'T-i-m-o-l-e-o-n-'
    >>> tirets('tirets dans la chaîne')
    't-i-r-e-t-s- -d-a-n-s- -l-a- -c-h-a-î-n-e-'
    """
    x =""
    for carac in str:
        x = x + carac +"-"
    return x

#q2
def tiretsv2(str):
    """
    renvoie une chaîne construite à partir de celle reçue en paramètre en
    insérant un tiret derrière chacun de ses caractères.
    :param str:(str) chaîne de caractères.
    :return x:(str) chaîne de caractères avec un tiret derrière chacun de
    ses caractères.
    :CU: None
    
    exemples:
    >>> tirets('Timoleon')
    'T-i-m-o-l-e-o-n-'
    >>> tirets('tirets dans la chaîne')
    't-i-r-e-t-s- -d-a-n-s- -l-a- -c-h-a-î-n-e-'
    """
    x =""
    for carac in str:
        if carac != " ":
            x = x + carac +"-"
        else:
            x = x + carac
    return x
            
#exercice 5

def miroir(str):
    """
    renvoie une chaîne contenant les caractères de la chaîne
    passée en paramètre dans l’ordre inverse.
    :param str:(str) chaîne de caractères.
    :return str: (str) chaîne contenant les caractères de la chaîne dans l'ordre
    :CU: None
    
    exemples:
    >>> miroir('Timoleon')
    'noelomiT'  
    """
    x = ''
    for carac in str:
        x = carac+ x
    return x

#exercice 6
#q1
def est_palindromique(str):
    """
    renvoie True si la chaîne passée en paramètre est palindromique, False dans le cas contraire.
    :param str:(str) chaîne de caractères
    :return x: (bool) renvoie True si la chaîne de caractères est palindromique et inversement.
    :CU: None
    
    exemples:
    >>> est_palindromique('test')
    False
    >>> est_palindromique('RADAR')
    True
    """
    x= ''
    for carac in str:
        x = carac+x
    return str == x
#q2
def est_palindromiquev2(str):
    """
    renvoie True si la chaîne passée en paramètre est palindromique, False dans le cas contraire.
    :param str:(str) chaîne de caractères
    :return x: (bool) renvoie True si la chaîne de caractères est palindromique et inversement.
    :CU: None
    
    exemples:
    >>> est_palindromique('test')
    False
    >>> est_palindromique('RADAR')
    True
    """
    return str == miroir(str)

#exercice 7
#q1
def supprimerOccCarac(str,chara):
    """
    renvoie une chaîne obtenue en supprimant toutes les occurrences d’un caractère
    dans une chaîne, ce caractère et cette chaîne étant passés en paramètre.
    Si le caractère à supprimer ne se trouve pas dans la chaîne, la fonction
    renvoie la chaîne sans la modifier.
    :param str: (str) une chaîne de caractères.
    :param chara: (str) chaîne obtenue en supprimant toutes les occurrences d’un caractère
    dans la chaîne.
    :return x:(str) chaîne sans occurence.
    :CU: None
    
    exemples:
    >>> supprimerOccCarac('Timoleon', 'o')
    'Timlen'
    >>> supprimerOccCarac('Timoleon', 'y')
    'Timoleon' 
    """
    x =""
    for carac in str:
        if carac != chara:
            x = x + carac
    return x
#q2
#>>> est_palindromiquev2(supprimerOccCarac("esope reste ici et se repose"," "))
#True

#exercice 8
#q1
def mettreEnMajuscule(str):
    """
    transforme toutes les lettres majuscules non accentuées d'une chaîne
    en lettres minuscules. Les autres caractères restent inchangés.
    :param str: (str) chaîne de caractères.
    :return x: (str) chaîne de caractères entièrement en majuscules.   
    :CU: None
    
    exemples:
    >>> mettreEnMajuscule('Abcé,3 @!-xyZ')
    'ABCé,3 @!-XYZ'
    """
    x=""
    for carac in str:
        if carac >= "a" and carac <= "z":
            x = x + chr(ord(carac) - 32)
        else:
            x= x+carac
    return x

#exercice 9

def mettreEnMinuscule(str):
    """
    transforme toutes les lettres minuscules non accentuées d'une chaîne en
    lettres majuscules. Les autres caractères restent inchangés.
    :param str: (str) chaîne de caractères.
    :return x:(str) chaîne de caractères entièrement en minuscules.
    :CU: None
    
    :exemples:
    >>> mettreEnMinuscule('aBC\u00c9,3 @!-XYz')
    'abcÉ,3 @!-xyz'   
    """
    x=""
    for carac in str:
        if carac >= "A" and carac <= "Z":
            x = x + chr(ord(carac) + 32)
        else:
            x= x+carac
    return x

#exercice 10
#q1
def transformerMinMaj(str):
    """
    change la casse des caractères de la chaîne passée en paramètre. Les lettres
    en minuscule non accentuées passent en majuscule et inversement. Les autres
    caractères restent inchangés.
    :param str:(str) chaîne de caractères.
    :return x: (str) chaîne de caractères, où les minuscules deviennent
    majuscules et inversement.
    :CU: None
    
    exemples:
    >>> transformerMinMaj('aBC\u00c9,3 @!-XYz')
    'AbcÉ,3 @!-xyZ'  
    """
    x=""
    for carac in str:
        if carac >= "A" and carac <= "Z":
            x = x + chr(ord(carac) + 32)
        elif carac >= "a" and carac <= "z":
            x = x + chr(ord(carac) - 32)
        else:
            x= x+carac
    return x

#exercice 11
def comparerChaines(str1,str2):
    """
    effectue la comparaison de deux chaînes. Cette fonction prendra en paramètre
    deux chaînes de caractères et retournera une valeur entière:
    -0 en cas d’égalité des chaînes.
    -1 si la première chaîne de caractères est supérieure alphabétiquement à la seconde,
    -2 si la seconde chaîne de caractères est supérieure alphabétiquement à la première.

    :param str1: (str) première chaîne de caractère.
    :param str2: (str) deuxième chaîne de caractère.
    :return 0 or 1 or 2: (int)
    :CU: None
    
    exemples:
    >>> comparerChaines("texte", "texte") 
    0
    >>> comparerChaines("texto", "texte")
    1
    """
    if str1 == str2:
        return 0
    if str1 > str2:
        return 1
    else:
        return 2
            
#exercice 12
#q1
def rechercherCaractereG(stri,chara):
    """
    renvoie l'indice de la première occurrence d’un caractère dans une chaîne en partant de la gauche.
    Cette fonction prend en entrée la chaîne de caractères ainsi que le caractère recherché.
    Elle retourne l'indice du caractère si il est présent dans la chaîne, et la valeur -1 si le caractère n’a pas été trouvé.
    :param stri: (str) chaîne de caractère.
    :param chara: (str) indice
    :return carac: (str) indice du caractère si il est présent dans la chaîne, et la valeur -1 si le caractère n’a pas été trouvé.
    :CU: None
    
    exemples:
    >>> rechercherCaractereG('voici une chaîne', 'i')
    2
    >>> rechercherCaractereG('voici une chaîne', 'z')
    -1
    """
    i = 0
    for carac in stri:
        if carac == chara:
            return i
        else:
            i +=  1
    return -1
#q2
def rechercherCaractereD(stri,chara):
    """
    :param stri: (str) une chaîne de caractère
    :param chara: (str) un caractère
    :return i: (int) un indice
    :CU: None
    
    exemples:
    >>> rechercherCaractereD("ami","i")
    2
    """
    i= len(stri) - 1
    while i>= 0:
        if stri[i] == chara:
            return i
        else:
            i = i-1
    return -1

#q3
def rechercherCaractereG_v2(stri,chara):
    """
    renvoie l'indice de la première occurrence d’un caractère dans une chaîne en partant de la gauche.
    Cette fonction prend en entrée la chaîne de caractères ainsi que le caractère recherché.
    Elle retourne l'indice du caractère si il est présent dans la chaîne, et la valeur -1 si le caractère n’a pas été trouvé.
    :param stri: (str) chaîne de caractère.
    :param chara: (str) indice
    :return carac: (str) indice du caractère si il est présent dans la chaîne, et la valeur -1 si le caractère n’a pas été trouvé.
    :CU: None
    
    exemples:
    >>> rechercherCaractereG('voici une chaîne', 'i')
    2
    >>> rechercherCaractereG('voici une chaîne', 'z')
    -1
    """
    i = 0
    rep= ""
    oui = miroir(stri)
    for carac in oui:
        if stri[i]== chara:
            return i
        else:
            i += 1
    return -1

#exercice 13
def nbreOccurrences(chara,str):
    """
    renvoie le nombre d’occurrences d’un caractère dans une chaîne, le caractère et la chaîne étant passés en paramètre.
    :param chara: (str) caractère
    :param str: (str) chaîne de caractères
    :return z: (int) nombre d'occurence du caractère
    :CU: None
    
    exemples:
    >>> nbreOccurrences('o', 'Timoleon')
    2
    >>> nbreOccurrences('y', 'Timoleon')
    0
    """
    z = 0
    for carac in str:
        if carac == chara:
            z += 1
    return z


#exercice 14
#q1
def plusFrequent(stri):
    """
    renvoie l'indice de la première occurrence d’un caractère dans une chaîne en partant de la gauche.
    Cette fonction prend en entrée la chaîne de caractères ainsi que le caractère recherché.
    Elle retourne l'indice du caractère si il est présent dans la chaîne, et la valeur -1 si le caractère n’a pas été trouvé.
    :param stri: (int) chaîne de caractères.
    :param carac: (str) lettre qui possède la plus grande occurence.
    """
    alphabet="abcdefghijklmnopqrstuvwxyz"
    z=0
    for carac in stri:
        if carac in alphabet:
            z+= 1
    return carac

#exercice 15
#q1
def supprimerCarac(stri,indice):
    """
    renvoie la chaîne obtenue en supprimant le caractère d’indice i d’une chaîne s, ces deux éléments étant passés en paramètres.
    :param stri:(str) une chaîne de caractères
    :param indice: (int) l'indice
    :return rep: (str) la chaîne de caractères avec le caractères avec l'indice correspondant, supprimé.
    :CU: None
    
    exemples:
    >>> supprimerCarac('Timoleon', 3)
    'Timleon'
    """
    une_fois= False
    rep= ""
    for carac in stri:
        if indice >= len(stri) or indice <= 0:
            rep= stri
        elif carac == stri[indice] and une_fois == False:
            rep = rep
            une_fois = True
        elif carac == stri[indice] and une_fois == False:
            rep += carac
        else:
            rep += carac
    return rep

#q2
def supprimerCarac_v2(stri,indice):
    """
    renvoie la chaîne obtenue en supprimant le caractère d’indice i d’une chaîne s, ces deux éléments étant passés en paramètres.
    :param stri:(str) une chaîne de caractères
    :param indice: (int) l'indice
    :return rep: (str) la chaîne de caractères avec le caractères avec l'indice correspondant, supprimé.
    :CU: None
    
    exemples:
    >>> supprimerCarac_v2('Timoleon', 7)
    'Timoleo'
    >>> supprimerCarac_v2('Timoleon', -1)  
    'Timoleo'
    """
    une_fois= False
    rep= ""
    for carac in stri:
        if indice < -len(stri) or indice >= len(stri):
            return stri
        elif carac== stri[indice] and une_fois== False:
            rep = rep
            une_fois == True
        elif carac == stri[indice] and une_fois == False:
            rep += carac
        else:
            rep += carac
    return rep


#exercice 16
def insererCaractere(stri,indice,chara):
    """
    renvoie la chaîne obtenue en insérant dans la chaîne reçue en premier paramètre, à l'indice passé en second paramètre,
    le caractère fourni en troisième paramètre. On suppose que l’indice est un entier positif ou nul. Si l'indice est en dehors
    de la chaîne, celle-ci devra être retournée sans être modifiée.
    :param stri: (str) une chaîne de caractères.
    :param indice: (int) un indice
    :param chara: (str) un caractère
    :return rep: (str) renvoie une chaîne de caractère ou l'on a insérer le caractère à tel indice indiqué.
    :CU: None
     
    exemples:
    >>> insererCaractere('Timleon', 3, 'o')
    'Timoleon'
    """
    rep= ""
    for carac in stri:
        if indice> len(stri):
            return stri
        elif carac == stri[indice - 1]:
            rep += carac + chara
        else:
            rep += carac
    return rep


#exercice 17
#q1
def remplacerCaractere(stri,indice,chara):
    """
    renvoie la chaîne reçue en premier paramètre après avoir remplacé dans celle-ci le
    caractère pointé par l'indice donné en second paramètre par la chaîne passée en troisième paramètre.
    :param stri: (str) une chaîne de caractères.
    :param indice: (int) un indice
    :param chara: (str) un caractère
    :return rep: (str) remplace un caractère d'une chaîne de caractère à tel indice, par le caractère rentré en paramètre.
    :CU: None
    
    exemples:
    >>> remplacerCaractere('Tim-leon', 3, 'o')
    'Timoleon'
    >>> remplacerCaractere('Ti-on', 2, 'mole')
    'Timoleon'
    """
    rep=""
    for carac in stri:
        if indice> len(stri):
            return stri
        elif carac==stri[indice]:
            rep+= chara
        else:
            rep+= carac
    return rep
#q2
def remplacerOccurrences(stri,occurence,chara):
    """
    remplace dans une chaîne donnée toutes les occurences d’un caractère donné par une autre chaîne de caractères.
    :param stri: (str) une chaîne de caractères
    :param occurence: (str) un caractère
    :param chara: (str) un caractère
    :return rep:(str) remplace dans une chaîne donnée toutes les occurences d’un caractère donné par une autre chaîne de caractères.
    :CU: None
    
    exemples:
    >>> remplacerOccurrences('@ 3 est le neveu de @ 1er.','@','Napoléon')
    'Napoléon 3 est le neveu de Napoléon 1er.'
    """
    rep= ""
    for carac in stri:
        if carac == occurence:
            rep += chara
        else:
            rep += carac
    return rep
                
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)