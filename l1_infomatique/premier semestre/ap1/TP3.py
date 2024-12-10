#tp3
import doctest
#lesaffre maeva

#Années bissextiles
#q1
def est_divisible(x,y):
    """
    prédicat qui renvoit True si le premier paramètre est divisible par le second, dans le cas contraire, il renvoit False.
    :x: (int or float) le nombre qui va être divisé.
    :y: (int or float) le nombre qui va diviser.
    :return: (booleen) retourne si le premier resultat est divisible par le second .
     
    :CU: None
    exemples:
    >>> est_divisible(-50,10)
    True
    >>> est_divisible(3,5)
    False
    """
    return x%y==0

#q2
def est_bissextile(x):
    """
    retourne  Vrai ou Faux si l'année passée en paramètre est bissextile ou non.
    :x: (int) une année
    :return: (booleen) retourne un vrai ou faux si l'année passée en paramètre est bissextile ou non.
    
    CU: x > 0
    
    exemples:
    >>> est_bissextile(2100)
    False
    >>> est_bissextile(4000)
    True
    """
    return x%4 == 0 and x%100 != 0 or x%400 == 0


#Nombre de jours dans un mois
#q3
def nbre_jour(mois,année):
    """
    Ce programme renvoie le nombre de jours du mois entré pour l'année entrée.
    : param mois: (int) le numéro du mois
    : param année: (int) l'année
    : return: (int) retourne le nombre de jours dans le mois.
    
    CU: 1> = mois> = 12
    
    Exemples:
    >>> nbre_jour(2,2016)
    29
    >>> nbre_jour(5,1560)
    31
    >>> nbre_jour(8,2017)
    31
    """
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
        return 31
    elif mois==2 and est_bissextile(année):
        return 29
    elif mois==2 and not est_bissextile(année):
        return 28
    else:
        return 30
        


#Date valide  
#q4
def est_date_valide(jour,mois,année):
    """
    Ce programme revient si la date entrée est valide ou non.
    : param jour: (int) le numéro du jour
    : param mois: (int) le numéro du mois 
    : param année: (int) l'année
    : return: retourne (booléen) si la date entrée est correcte ou non.
    
    CU: None
    
    Exemples:
    >>> est_date_valide(1,3,2015)
    True
    >>> est_date_valide(1.2,3,2015)
    False
    >>> est_date_valide(30,52,2018)
    False
    """
    return 0<jour<=nbre_jour(mois,année) and 0<mois<12 and type(jour)== type(mois) == type(année) == int
#q6
def corrige_mois(mois,année):
    """
    Ce programme renvoie la valeur correspondant au mois selon le tableau de la formule de Delambre.
    : param mois: (int) le numéro du mois
    : param année: (int) l'année
    : return: (int) retourne le numéro du mois correspondant
    
    CU: None
    
    Exemples:
    >>> corrige_mois(12,2016)
    2
    >>> corrige_mois(2,2015)
    0
    """
    if mois==1:
        if est_bissextile(année)== True:
            return 3
        else:
            return 4
    if mois==2:
        if est_bissextile(année)== True:
            return 6
        else:
            return 0
    elif mois==3:
        return 0
    elif mois==4:
        return 3
    elif mois==5:
        return 5
    elif mois==6:
        return 1
    elif mois==7:
        return 3
    elif mois==8:
        return 6
    elif mois==9:
        return 2
    elif mois==10:
        return 4
    elif mois==11:
        return 0
    elif mois==12:
        return 2
    else:
        return "mois non valide."
    
#q6
#>>> (4+5+19+2+23+2+5*20)%7
#1
    
    
#q7
def num_jour(jour,mois,année):
    """
    Ce programme renvoie la valeur correspondant au jour selon la formule de Delambre.
    : param jour: (int) le numéro du jour
    : param mois: (int) le numéro du mois
    : param année: (int) l'année
    : return: (int) retourne la valeur correspondant au jour.
    
    CU: None
    
    Exemples:
    >>> num_jour(4,6,2000)
    0
    >>> num_jour(26,8,1596)
    1
    """
    if est_date_valide(jour,mois,année):
        ab = année//100
        cd = année%100
        return int(((cd)/4 + (ab)/4 + cd + corrige_mois(mois,année) + jour + 2 + 5*(ab))% 7)
    
#q8
def nom_jour(jour,mois,année):
    """
    Ce programme renvoie le nom du jour entré.
    : param jours: (int) le numéro du jour
    : param mois: (int) le numéro du mois
    : param année: (int) l'année
    : return: (str) retourne le jour
    
    CU: None
    
    Exemples:
    >>> nom_jour(15,9,1954)
    'jeudi'
    >>> nom_jour(30,1,1632)
    'vendredi'
    """
    if num_jour(jour,mois,année)==0:
        return "dimanche"
    elif num_jour(jour,mois,année)==1:
        return "lundi"
    elif num_jour(jour,mois,année)==2:
        return "mardi"
    elif num_jour(jour,mois,année)==3:
        return "mercredi"
    elif num_jour(jour,mois,année)==4:
        return "jeudi"
    elif num_jour(jour,mois,année)==5:
        return "vendredi"
    elif num_jour(jour,mois,année)==6:
        return "samedi"
    else:
        return "on a pas de jours en plus"
            
    
    
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)   