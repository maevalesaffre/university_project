#TP4
#Lesafffe maeva
import doctest
##exercice 1##
#q1
def estADN(ch_caractere):
    """
    Vérifie si la chaîne passée en paramètre ne contient que les caractères A, C, G ou T.
    : param ch_caractere: (str) une chaîne
    : return : (Boolean) renvoie true si la chaîne contient les caractères uniquement A, C, G ou T.
    CU: None
    
     :Exemples:
     >>> estADN("ATCCCGTCA")
     True
     >>> estADN("ATECCGyTCA")
     False
     >>> estADN("")
     True
    """
   
    rep = 1
    for chara in ch_caractere:
        if chara != "A" and chara != "C" and chara != "G" and chara != "T":
            rep = 0
            
    return rep == 1
        
#q2
def transcrit(ch_caractere):
    """
    Vérifie si la chaîne entrée est une séquence d'ADN et construit une séquence d'ARN à partir de celle-ci (elle remplace tout T dans U).
    : param ch_caractere: (str) une chaîne
    : return ch_caractere: (str) retourne la séquence de ARN
    Cu: None
    
    :Exemples:
    >>> transcrit('ACGGTAGCTAGTTTCGACTGGAGGGGTA')
    'ACGGUAGCUAGUUUCGACUGGAGGGGUA'
    
    """
    RNA = ""
    if estADN(ch_caractere):
        for carac in ch_caractere :
            if carac == 'T' :
                RNA += 'U'
            else:
                RNA += carac
    return RNA

#q3
def baseComplementaire(ch_caractere):
    """
    Retourne la base complémentaire de la séquence de ADN passée en paramètre.
    : param ch_caractere: (str) séquence de ADN
    :return: Retourne la base complémentaire de la séquence de ADN.
    Cu: None
    
    :Exemples:
    >>> baseComplementaire("ACGGTAGCTAGTTTCGACTGGAGGGGTA")
    'TGCCATCGATCAAAGCTGACCTCCCCAT'
    """
    complementaire=""
    if estADN(ch_caractere):
        for carac in ch_caractere :
            if carac=="A":
                complementaire+="T"
            elif carac=="T":
                complementaire+="A"
            elif carac=="G":
                complementaire+="C"
            elif carac=="C":
                complementaire+="G"
    return complementaire

#q4
def sequenceComplementaireInversee(ch_caractere):
    """
    Vérifie si la chaîne entrée en tant que paramètre est une séquence d'ADN et renvoie la séquence complémentaire inversée de celle-ci.
    : param ch_caractere: (str) une chaîne.
    : return inverse: (str) retourne la séquence complémentaire inversée.
    
    Cu: None
    
    :Exemples:
     >>> sequenceComplementaireInversee ('ACTG')
     'CAGT'
    """
    inverse=""
    if estADN(ch_caractere):
        ch_caractere= baseComplementaire(ch_caractere)
        for carac in ch_caractere:
            inverse= carac+inverse
        return inverse
#q5
def nombreOccurrencesCodon(codon,ch_caractere):
    """
    Retourne le nombre de fois que le codon passe en tant que paramètre apparaît dans la séquence d'ARN également passée en paramètre.
    : param codon: (str) une longueur de 3 cordes
    : param ch_caractere: (str) une séquence ARN
    : return nb: (int) le nombre de fois que le codon apparaît
    
    Cu:None
    :Exemples:
    >>> nombreOccurrencesCodon('UUC', 'AGUUCGACUU')
    0
    >>> nombreOccurrencesCodon('ACG', 'GCUACGGAGCUUCGGAGCACGUAG')
    2
    """
    i = 0
    nb = 0
    if len(ch_caractere) % 3 == 0:
        while i <= len(ch_caractere):
            if ch_caractere[i: i+3] == codon:
                nb +=1
            i += 3
        return nb
    else:
        return 0
    
#q6
def analyse_ADN():
    """
    Ce programme demande de saisir une séquence d’ADN et un codon puis affiche les séquences complémentaires inversées.
    et l’ARN associé à la séquence d’ADN qui vient d’être entrée.Enfin, le programme indiquait le nombre d’occurrences
    du codon dans la séquence d'ARN.
    Si l'utilisateur entre une séquence d'ADN non valide, le programme imprime une erreur et s'arrête immédiatement.
    : retour: None
    Cu: None
    """
    ADN=input("entrez votre séquence ADN:")
    if estADN(ADN):
        codon=input("entrez votre codon:")
        print("la séquence complementaire Inversée:", sequenceComplementaireInversee(ADN))
        ARN=transcrit(ADN)
        print("ARN séquence :",ARN)
        print("Le codon apparaît", nombreOccurrencesCodon(codon,ARN), "fois dans la séquence ARN",)
    else:
        print("Séquence ADN erronée !!!")
    
##Exercice 2##          
#q1  pour savoir si une expression est bien parenthesée, à chaque parenthèses ouvertes, on lui attribue la valeur +1 et à chaque parenthèses fermantes,-1.
#    la somme renvoie 0 si l'expression est bien parenthesée, et l'expression de doit pas se termnier par une parenthèse ouverte.  

#q2
def bien_parenthesee(s):
    """
    Retourne True si la chaîne passée en tant que paramètre est bien parenthesée, et False sinon.
    
    : param s: (str) une chaîne de caractères
    : return: (boolean) True si c'est bien parenthesée, False sinon.
    
    Cu: None
    
    :Exemples:
    >>> bien_parenthesee("((())")
    False
    >>> bien_parenthesee("((() ()))")
    True
    """
    nb=0
    for carac in s:
        if carac== '(':
            nb+=1
        elif carac== ')':
            nb-=1
    if nb==0:
        return True
    else:
        return False

#def bien_parenthesee(s):
#    nb=0
#    for carac in s:
#        if carac== '(':
#            nb+=1
#        elif carac== ')':
#            nb-=1
#    if s[-1]== '(':
#        nb=1
#    return nb==0            
        

#q3
def nbre_facteurs(s):
    """
    Calcule le nombre de facteurs contenus dans une expression bien formée.
    : param s: (str) une chaîne de caractères.
    : return: (int) le nombre de facteurs.
    
    CU: None
    
    :Exemples:
    >>> nbre_facteurs('(() ())')
    3
    >>> nbre_facteurs("(()) ()")
    2
    >>> nbre_facteurs("(()) () (() ())")
    6
    """
    nb=0
    p=0
    if bien_parenthesee(s):
        for carac in s:
            if carac=='(':
                p=+1
            elif carac==')':
                p-=1
            if p== 0:
                nb+=1
        return nb



#q4    
def affiche_facteurs(s):
    """
    Imprimer tous les facteurs d’expression bien formée et d’insertion entre les caractères *
    :param s: (str) une chaîne
    :return: None

    Cu: None

    :Exemples:
    >>> affiche_facteurs('(()) () (() ())')
    (())* *()* *(() ())*
    >>> affiche_facteurs('() (() ())')
    ()* *(() ())*
    >>> affiche_facteurs('(()) () (() ())')
    (())* *()* *(() ())*
    """
    result = ""
    fac = ''
    nb = 0
    p = 0
    if bien_parenthesee(s):
        for carac in s:
            if carac == "(":
                p +=1
            elif carac == ")":
                p -=1
            fac += carac 
            if p == 0:
                result = result + fac + "*"
                fac = ''
        print(result)
        
        
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)
        
        