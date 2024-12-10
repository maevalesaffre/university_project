#TP6 Lesaffre maeva
from cent_mille import CENT_MILLE_MILLIARDS
from random import randint
import doctest
TUX = "   \\\n    \\\n        .--.\n       |o_o |\n       |:_/ |\n      //   \\ \\\n     (|     | )\n    /'\_   _/`\\\n    \___)=(___/"

def length_longest(tu):
    """
    retourne la longueur de la plus grande chaîne dans le tuple. Si le tuple est vide, elle renvoie -1.
    :param tu: (str) chaînes de caractères
    :return taille1: (int) la longueur de la plus grande chaîne de caractères.
    :CU: None
    
    :exemples:
    >>>length_longest(("Cher-e-s étudiant-e-s,", "", "Vous programmez très bien !"))
    27
    >>>length_longest(())
    -1
    """
    tu = tuple(tu)
    taille1 = -1
    for i in tu:
        taille2= len(i)
        if taille2 >=taille1:
            taille1 = taille2
    return taille1
        
def dash_line(n_tirets):
    """
    retourne une chaîne de caractères composée d'un espace suivi par n_tirets tirets.
    :param n_tirets:(int) un entier
    :return string1: (str) une chaîne de caractère composée de 1 espace pis n_tirets tiret.
    :CU: None
    
    :exemples:
    >>>dash_line(29)   
    ' -----------------------------'
    """
    string=" "
    string1 = string+n_tirets*"_"
    return string1
    
def msg_line(msg,largeur):
    """
    retourne une chaîne de caractères débutant par un | et suivi d'un espace, puis de la chaîne msg écrite sur largeur
    caractères (des espaces sont ajoutés à la fin, si nécessaire), suivie par un espace et un |.
    :param msg:(str): une chaîne de caractère.
    :param largeur: (int) un entier
    :return :(int) chaîne de caractère.
    :CU: None
    
    :exemples:
    >>> msg_line("Cher-e-s étudiant-e-s,", 27)
    '| Cher-e-s étudiant-e-s,      |'   
    """
    while len(msg)<=largeur:
        msg+= " "
    return "| "+msg+" |"

def tux_say(tu):
    """
    imprime dans une bulle les chaînes de caractères du tuple. La largeur de la bulle devra s'adapter
    à la largeur de la plus grande des chaînes du tuple.
    :param tu:(str)
    :return TUX: un pingouin et une bulle de discussion avec tu inscrit dedans
    :CU: None
    
    :exemples:
    >>> tux_say (("Cher-e-s étudiant-e-s,", "", "Vous programmez très bien !"))
     -----------------------------
    | Cher-e-s étudiant-e-s,      |
    |                             |
    | Vous programmez très bien ! |
     -----------------------------
       \
        \
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/
    """
    if len(tu) >0:
        print(dash_line(largeur+2))
        for i in tu:
            print(msg_line_center(i,largeur))
        print(dash_line(largeur+2))
    else:
        print(dash_line(3))
        print( msg_line_center("?",1))
        print(dash_line(3))
    print(TUX)
        
def un_poeme():
    """
    retournant un tuple de quatorze vers choisis au hasard (le premier ayant été choisi au hasard
    parmi les 10 premières chaînes, le deuxième parmi les 10 suivantes, jusqu'au quatorzième choisi
    au hasard parmi les 10 dernières du tuple CENT_MILLE_MILLIARDS. Vous séparerez les quatrains et
    les tercets par une ligne vide.
    :return a,b,c,d,e,f,g,h,i,j,k,l,m,n: (tuple) tuple de chaînes de caractère.
    :CU: None
    
    :exemples:
    >>>tux_say(un_poeme())
     ------------------------------------------------------
    | Lorsque tout est fini lorsque l'on agonise           |
    | pour consommer un thé puis des petits gâteaux        |
    | il se penche et alors à sa grande surprise           |
    | on espère toujours être de vrais normaux             |
    |                                                      |
    | On était bien surpris par cette plaine grise         |
    | où venaient par milliers s'échouer les harenceaux    |
    | l'un et l'autre ont raison non la foule imprécise    |
    | la mite a grignoté tissus os et rideaux              |
    |                                                      |
    | Devant la boue urbaine on retrousse sa cotte         |
    | le chat fait un festin de têtes de linotte           |
    | le colonel s'éponge un blason dans la main           |
    |                                                      |
    | Sa sculpture est illustre et dans le fond des coques |
    | les Indes ont assez sans ça de pendeloques           |
    | toute chose pourtant doit avoir une fin              |
     ------------------------------------------------------
       \
        \
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/
    """
    a = CENT_MILLE_MILLIARDS[randint(0,9)]
    b = CENT_MILLE_MILLIARDS[randint(10,19)]
    c = CENT_MILLE_MILLIARDS[randint(20,29)]
    d = CENT_MILLE_MILLIARDS[randint(30,39)]
    e = CENT_MILLE_MILLIARDS[randint(40,49)]
    f = CENT_MILLE_MILLIARDS[randint(50,59)]
    g = CENT_MILLE_MILLIARDS[randint(60,69)]
    h = CENT_MILLE_MILLIARDS[randint(70,79)]
    i = CENT_MILLE_MILLIARDS[randint(80,89)]
    j = CENT_MILLE_MILLIARDS[randint(90,99)]
    k = CENT_MILLE_MILLIARDS[randint(100,109)]
    l = CENT_MILLE_MILLIARDS[randint(110,119)]
    m = CENT_MILLE_MILLIARDS[randint(120,129)]
    n = CENT_MILLE_MILLIARDS[randint(130,139)]
    return (a,b,c,d," ",e,f,g,h," ",i,j,k," ",l,m,n)                
            
            
# doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)        
    
    
    