#BUlois Melanie
#groupe22
#TP3
 
#Anne bissextiles

#Q1
def est_divisible(A,B):
    """
    renvoie 'True' si A est divible par B
    renvoie 'False' si A n'est pas divisible apr B
    :param A:(int) un nombre entier
    :param B:(int) un nombre entier
    :return: 'True' or 'False'
    C.U: aucune
    
    exemple:
    
    >>> est_divisible(3,9)
    False
    >>> est_divisible(9,3)
    True
    
    """
    if A % B == 0:
        return True
    else:
        return False
    

#Q2
    
def est_bissextile(annee):
    """
    renvoie 'True' si l'annee est bissextile
    renvoie'false' si l'annee n'est pas bissextile
    :parm annee:(int) une annee
    :return:(bool)
    C.U: aucune
    
    exemple :
    >>> est_bissextile(2016)
    True
    >>> est_bissextile(2017)
    False
    
    """
    if annee % 400 == 0:    
        return True
    elif annee % 4 ==0 and annee % 100 !=0:
        return True
    else:
        return False
#Nombre de jours dans un mois    
#Q3
def nbre_jours (m,a):
    """
    renvoie le nombre de jours par mois selon les annee
    :param m:(int)un mois
    :param a:(int)une annee
    :return:(int) le nombre de jours dans le mois
    C.U: 0<m<13
    
    exemple:
    >>> nbre_jours(1,2017)
    31
    >>> nbre_jours(2,2017)
    28
    >>> nbre_jours(3,2017)
    31
    >>> nbre_jours(4,2017)
    30
    >>> nbre_jours(5,2017)
    31
    >>> nbre_jours(6,2017)
    30
    >>> nbre_jours(7,2017)
    31
    >>> nbre_jours(8,2017)
    31
    >>> nbre_jours(9,2017)
    30
    >>> nbre_jours(10,2017)
    31
    >>> nbre_jours(11,2017)
    30
    >>> nbre_jours(12,2017)
    31
    >>> nbre_jours(2,2016)
    29
    
    """
    nbre=0
    if m == 1 or m ==3 or m ==5 or m ==7 or m ==8 or m ==10 or m ==12 :
        nbre=31
    elif m == 4 or m ==6 or m ==9 or m ==11 :
        nbre=30
    else:
        if a % 400 == 0:    
            nbre=29
        elif a % 4 ==0 and a % 100 !=0:
            nbre=29
        else:
            nbre=28
    return nbre
#Date valide
#Q4

def est_date_valide(j,m,a):
    """
    renvoie True si la date existe
    renvoie False si elle n'existe pas
    :param j:(int) un jour
    :param m:(int) un mois
    :param a:(int) une annee
    :return:(bool)
    C.U: aucune
    
    exemple:
    
    >>> est_date_valide(1,2,2019)
    True
    >>> est_date_valide(1,13,2019)
    False
    
    """
    if j<=31 and m<=12:
        return True
    else:
        return False
    
#Nuemro du jour dans la semaine
#Q5

#>>> (4+5+19+2+24+2+5*20)%7
#2

#Q6

def corrige_mois(m,a):
    """
    renvoie la valeur corriger du mois selon l'annee
    :param m:(int) un mois
    :param a:(int) une annee
    :return:(int) la valeur du mois corriger
    C.U: 0<m<13 et a=>0
    
    Exemple:
    
    >>> corrige_mois(9,2019)
    2
    >>> corrige_mois(2,2016)
    6
    """
    if m==1:
        if est_bissextile(a)==True:
            return 3
        else:
            return 4
    elif m==2:
        if est_bissextile(a)==True:
            return 6
        else:
            return 0
    elif m==3:
        return 0
    elif m==4:
        return 3
    elif m==5:
        return 5
    elif m==6:
        return 1
    elif m==7:
        return 3
    elif m==8:
        return 6
    elif m==9:
        return 2
    elif m==10:
        return 4
    elif m==11:
        return 0
    elif m==12:
        return m==2
    else:
        return "invalide"
    
#Q7
def num_jour(j,m,a):
    if est_date_valide(j,m,a):
        ab=a//100
        cd=a%100
    