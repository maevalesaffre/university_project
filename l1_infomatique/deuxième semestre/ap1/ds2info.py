#exercice 1
#q1
#s.split(;)

#q2
#" ".join(l_chaines)

#q3
def entier(n):
    """
    CU: None
    """
    liste=list()
    for i in range(0,n):
        if i%2==0:
            liste+=""
        else:
            liste+=[i,]
    return liste
#q4 à revoir
def entier_divisible_par_3(l_entiers):
    """
    CU: None
    """
    new_list=list()
    for i in l_entiers:
        if i/3==0:
            new_list+=[i,]
        else:
            new_list=[i,]
    return new_list
            
#q5
#[(x,y) for x in liste for y in liste if x==y]

#q6
#[(x,y) for x in liste for y in liste if y-x==1]
#q7
#[(x,y) for x in liste for y in liste]
#q8
liste_infos_pays = [('AD', 'Andorra', 468.0, 84000, 'EU'), ('AE', 'United Arab Emirates', 82880.0, 4975593, 'AS'), ('AF', 'Afghanistan', 647500.0, 29121286, 'AS')] 
def creer_dico(liste_infos_pays):
    """
    CU: None
    """
    dico_infos_pays=dict()
    for i in liste_infos_pays:
        dico_infos_pays.update({i[0]:(i[1],i[2],i[3],i[4])})
    return dico_infos_pays
    
#q9
d=creer_dico(liste_infos_pays)
def ensemble_des_pays(d):
    """
    CU: None
    """
    liste_pays=list()
    i=0
    liste=list()
    for i in d:
        liste_pays+=[d[i][0],]
    return set(liste_pays)
        
#q10
def calculer_population(d):
    """
    CU: None
    """
    toto=int()
    for i in d:
        toto+=d[i][2]
    return toto
        
#q11
def calcul_par_pays(d):
    """
    CU:None
    """
    toto=0
    for i in d:
        if d[i][3]=='AS':
            toto+=1
    return toto


#exercice 2
#q1
phrase="Timoleon est un homme politique grec."
def nbre_occurrences(car, texte, deb, fin):
    """
    renvoie le nombre d'occurrences du caractère car dans la chaîne
    texte entre les indices deb inclus et fin exclu
    :param car:(str) un caractère
    :param texte:(str) une chaîne de caractère
    :param deb:(int) indice du début
    :param fin:(int) indice de fin
    :return nb_occ:(int) nombre d'occurence de car dans le texte texte.
    :CU: None
    
    exemple:
    >>> nbre_occurrences('o', phrase, 0, len(phrase))
        4
    >>> nbre_occurrences('o', phrase, 4, 18)
        2
    >>> nbre_occurrences('o', phrase, 3, 3)
        0   
    """
    nb_occ=0
    new_phrase=texte[deb:fin]
    for carac in new_phrase:
        if carac==car:
            nb_occ+=1
    return nb_occ
    
#q2
#Le nb de comparaison pour nbre_occurrences('o', phrase, 0, len(phrase)) est l=len(phrase)
#Le nb de comparaison pour nbre_occurrences('o', phrase, 4, 18) est l=18-4=14
#Le nb de comparaison pour nbre_occurrences('o', phrase, 3, 3) est l=0

#q3
def frequence(car,debut,fin,texte):
    d=nbre_occurrences(car,texte,debut,fin)
    return d/fin
    
#q5

    
    


    