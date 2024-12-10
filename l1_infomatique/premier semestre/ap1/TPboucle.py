#TP Boucle
#Lesaffre maeva
import doctest
#exo 1
#q1
def afficher_ligne(n):
    """
    affiche une ligne de n caractères 'O'
    :param n:(int) un entier
    :return x:(str) une chaîne de caractère
    :CU: n>0
    
    exemples:
    >>> afficher_ligne(5)
    00000  
    """
    x=""
    for carac in range(n):
        x=x+"0"
    print (x)

#q2
def afficher_carre(n):
    """
    affiche un carré de hauteur n avec des caractères 'O'
    :param n:(int) un entier
    :return res: (str) carré de chaînes de caractères
    CU: n>0
    
    exemples:
    >>> afficher_carre(5)
    00000
    00000
    00000
    00000
    00000
    """
    for carac in range (n):
        res=afficher_ligne(n)
    print (res)
        
#q3
def afficher_triangle_V1(n):
    """
    affiche un triangle de hauteur n
    :param n:(int) un entier
    :return res: (str) triangle de chaînes de caractères
    CU: n>0
    
    exemples:
    >>> afficher_triangle_V1(5)
    0
    00
    000
    0000
    00000
    """
    x=""
    for carac in range(n):
        x+="0"
        print(x)
        
#q4
def afficher_carre_diagonale(n):
    """
    affiche un carré de hauteur n avec une diagonale de caractères X
    :param n:(int) un entier
    :return str: (str) un carré de chaînes de caractères
    CU: n>0
    
    
    exemples:
    >>> afficher_carre_diagonale(5)
    X0000
    0X000
    00X00
    000X0
    0000X
    """
    compteur=0
    for carac in range(n):
        str=""
        for carac in range(0,n):
            if carac==compteur:
                str += "X"
            else:
                str += "0"
        compteur +=1
        print (str)
#q5
def afficher_triangle_V2(n):
    """
    affiche un triangle de hauteur n
    :param n:(int) un entier
    :return res: (str) triangle de chaînes de caractères
    CU: n>0
    
    exemples:
    >>> afficher_triangle_V2(5)
        0    
       0  0     
      0     0     
     0        0     
    000000000
    """
    L = n+n-1
    for ligne in range(0,n-1):
        str = ""
        chara = 1
        NbO = 0
        while len(str) < L:
            if chara == (n-ligne):
                str +="0"
                NbO +=1
                if NbO < (ligne+1):
                    for ligne in range(1,ligne+2*(ligne)):
                        str += " "
                    str += "0"
                    NbO += 1
                    for ligne in range(0,n):
                        str +=" "
            else:
                str  += " "
            chara+= 1
        print(str)
    str =""
    for g in range(0,L):
        str += "0"
    print(str)


#exercice 2
#q1
def table(n):
    """
    affiche la table de multiplication de n.
    :param n: (int) un entier
    :return 
    """
    x=0
    for carac in range(11):
        res=carac*n
        x+=1
        print (carac ,"x", n ,"=", res)
        
#q2
def tableAB(a,b):
    """
    affiche toutes les tables de multiplication pour les naturels de a à b.
    :param a: (int)un entier
    :param b: (int) un deuxième entier
    :return res: (str) des chaînes de caractères.
    :CU: a<b and a,b >0
    
    exemples:
    >>> tableAB (2,5)
    0 x 2 = 0
    1 x 2 = 2
    2 x 2 = 4
    3 x 2 = 6
    4 x 2 = 8
    5 x 2 = 10
    6 x 2 = 12
    7 x 2 = 14
    8 x 2 = 16
    9 x 2 = 18
    10 x 2 = 20
    None
    0 x 3 = 0
    1 x 3 = 3
    2 x 3 = 6
    3 x 3 = 9
    4 x 3 = 12
    5 x 3 = 15
    6 x 3 = 18
    7 x 3 = 21
    8 x 3 = 24
    9 x 3 = 27
    10 x 3 = 30
    None
    """
    for carac in range(a, b + 1):
        res=table(carac)
        print (res)

#exercice 3 
#q1
# "c" devient "m" et "car" devient "i", ce qui fait que le programme retourne False.


#q2
def est_present(c,s):
    """
    retourne un booléen si le caractère c est dans la chaîne s.
    :param c: (str) un caractère.
    :param s: (str) une chaîne de caractère.
    :return: (bool) True or False si le caractère c est dans la chaîne s.
    
    :CU: None
    
    exemples:
    >>> est_present('i','informatique')
    True
    >>> est_present('z','informatique')
    False
    """
    present = False
    for carac in s:
        if c == carac:
            present = True
        else:
            present = present
    return present
   
   
        
#exercice 14
def plus_long(str):
    """
    fonction qui donne le mot le plus long de la chaine de caractères. Si plusieurs mots sont solutions, peu importe celui qui est donné.
    :param str: (str) une chaîne de caractères.
    :return res: (str) le mot le plus long de la chaîne de caractères.
    :CU: None
    
    exemples:
    >>> plus_long('le matou silencieux prend son temps')
    'silencieux'   
    """
    stri1 = str.split()
    res=""
    for carac in stri1:
        if len(carac) > len(res):
            res= carac
    return res
                    
#exercice 16:
#q1
def decode(s):
    rep=""
    i= 0
    for c in s:
        if c=='0' or c=='1' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9':
            n= int(c)
            rep += n*s[i - 2]
        return rep
  
#q2
def encode(s):
    """
    retourne le code en fonction de la chaîne passée en paramamètres.
    :param s: (str) une chaîne de caractères.
    :return: (str) le code
    
    :CU: None
    
    """
    rep= ""
    while s!= '':
        current_char= s[0]
        compt= 0
        while compt < len(s) and s[compt] == current_char:
            compt += 1
            rep += current_char + str(compt)
            s = s[compt::]
        return rep

doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)            
            
        
        
       
           
           