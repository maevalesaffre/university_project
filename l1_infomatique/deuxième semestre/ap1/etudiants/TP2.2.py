from etudiants import L_ETUDIANTS
import doctest

#TP2
#Lesaffre Maeva
#Kernouf Sabrina

def pour_tous(l):
    """
    renvoie True si et seulement si tous les éléments de l’itérable passé en paramètre sont vrais et False dans le cas contraire.
    :param seq_bool:(list ou tuple) séquence de booléens
    :return: (bool) true si seq_bool ne contient pas le booléen False, false sinon
    :CU: none
    :exemple:
    >>> pour_tous([])
    True
    >>> pour_tous((True, True, True))
    True
    >>> pour_tous((True, False, True))
    False
    """
    for i in l:
        if i==False:
            return False
    return True

def il_existe(l):
    """
    renvoie True si et seulement si il existe un élément de l’itérable passé en paramètre qui est vrai et qui renvoie False dans le cas contraire.
    :param seq_bool:(list ou tuple) séquence de booléens
    :return: (bool) true si seq_bool contient le booléen True, false sinon
    :CU: none
    :exemple:
    >>> il_existe([])
    False
    >>> il_existe((False, True, False))
    True
    >>> il_existe((False, False))
    False
    """ 
    for i in l:
        if i==True:
            return True
    return False

#Question 0
COURTE_LISTE= L_ETUDIANTS[0:5]

#Question 1

def est_liste_d_etudiants(x):
    """
    verifie si x est bien une liste de dictionnaires
    :param x: (all) tout ce qu'on veut
    :return: (bool) True si c'est une liste de fiches étudiant, False dans le cas contraire
    :CU: none
    :Examples:
    >>> est_liste_d_etudiants(COURTE_LISTE)
    True
    >>> est_liste_d_etudiants("Timoleon")
    False
    >>> est_liste_d_etudiants([('12345678', 'Calbuth', 'Raymond', 'Danse', '12') ])
    False
    """
    key=('nip','nom','prenom','formation','groupe')
    for i in x:
        if type(i) != type(dict()):
            return False
        else:
            T= (element in i for element in key)
            return pour_tous(T)


#Question 2            
NBRE_FICHES=len(L_ETUDIANTS)
#>>> print(NBRE_FICHES)
#583

#Question 3
NIP= 41801943
fiche= NIP%NBRE_FICHES
#>>> print(L_ETUDIANTS[fiche])
#{'nip': '48366344', 'nom': 'Lebrun', 'prenom': 'Émile', 'formation': 'SESI', 'groupe': '43'}

#Question 4
def ensemble_des_formations(l):
    """
    Retourne l'ensemble des formations
    :param liste: (list) liste de fiche etudiante
    :return: (set) l'ensemble des formations
    :Cu: la liste ne contient que des fiches étudiants
    :Exemples:
    >>> Liste_demo = [{'nip' : '1174520', 'nom' : 'ERARD','prenom' : 'ANNAELLE', 'formation' : 'SESI', 'groupe' : '21'}]
    >>> Liste_demo.append({'nip' : '1171680', 'nom' : 'VASSEUR', 'prenom' : 'AGATHE', 'formation' : 'PEIP', 'groupe' : '12'})
    >>> Liste_demo.append({'nip' : '1170249', 'nom' : 'CARDOSO MORENO','prenom' : 'INEIDA', 'formation' : 'MASS', 'groupe' : '2'})
    >>> ensemble_des_formations(Liste_demo) == { 'SESI','PEIP','MASS' }
    True
    >>> ensemble_des_formations(Liste_demo[0:2]) == { 'SESI','PEIP' }
    True
    """
    formation=set()
    for i in l:
        etudiant=i["formation"]
        formation.add(etudiant)
    return formation
        
#Question 5
def nbre_prenom(liste,prenom):
    """
    Renvoie le nombre d'etudiant dont le prénom est passé en second parametre dans la liste d'étudiant
    passée en premier paramètre
    :param liste: (list) liste de fiches d'étudiants
    :param prenom: (str) un prénom
    :return: (int) le nombre d'etudiant ayant le prénom entré en parametre
    :Cu: none
    :Examples:
    >>> nbre_prenom(COURTE_LISTE, 'MOHAMED')
    0
    >>> nbre_prenom(COURTE_LISTE, 'ZENOBE')
    0
    """
    nbr = 0
    for etudiant in liste:
        prenomE = etudiant["prenom"]
        if prenomE == prenom:
            nbr += 1
    return nbr

#>>> nbre_prenom(COURTE_LISTE, 'Camille')
#0        
#>>> nbre_prenom(COURTE_LISTE, 'Alexandre')
#0


#Question 6
def nb_prenoms(liste):
    """
    renvoie le nombre de prenom différents parmis les éléves
    :param liste: (list) la liste de fiche etudiants
    :return: (int) le nombre de noms différent
    :Cu: la liste dois seulement contenir des fiches etudiants
    """
    prenoms = set()
    for etudiant in liste:
        prenomE = etudiant["prenom"]
        prenoms.add(prenomE)
    return len(prenoms)

#question 7
def freq_prenoms(liste):
    """
    Renvoie le prenom le plus courant de la liste et le nombre de fois qu'il apparait
    :param liste: (list) liste de fiche étudiant
    :return: (tuple) le prenoms et sont nombre d'occurence
    :Cu: la liste doit contenir que des fiches etudiants
    """
    count=dict()
    nb=0
    max=list()
    for carac in liste:
        prenomE = carac["prenom"]
        if prenomE in count:
            count[prenomE] += 1
        else:
            count[prenomE] =1
        for prenom in count:
            nbp= count[prenom]
            if nbp==nb:
                max.append(carac)
            elif nbp> nb:
                max=[carac]
                nb=nbp
        return max,nb
                
#>>> prenom_plus_frequent(L_ETUDIANTS)
#([{'nip': '49284201', 'nom': 'Remy', 'prenom': 'Anne', 'formation': 'SESI', 'groupe': '14'}], 1)                
#les plus fréquents Remy, et Anne

#Question 8
nip = list()
for etudiant in L_ETUDIANTS:
    nip.append(etudiant["nip"])
print(len(nip) == len(set(nip)) )


#Question 9
def etudiants_par_parcours(liste):
    count=dict()
    for carac in liste:
        formation=carac["formation"]
        if formation in count:
            count[formation] += 1
        else:
            count[formation]=1
    return count
    
    
#Question 10
def liste_formation(liste,form):
    """
    Construit la liste des étudiants de la formation entré en parametre, contient les quadruplets (nip, nom, prenom, gpe)
    :param liste: (list) une liste de fiche étudiants
    :param form: (str) une formation
    :return: la liste des étudiants de la formation form sous forme d’un quadruplet (nip, nom, prenom, groupe)
    :CU: none
    :Exemples:
    >>> len(liste_formation(L_ETUDIANTS, 'INFO'))
    0
    """
    liste_etudiant = list()
    for etudiant in liste:
        formation = etudiant["formation"]
        if formation == form:
            del etudiant["formation"]
            liste_etudiant.append(tuple(etudiant))
    return liste_etudiant        
               
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True) 