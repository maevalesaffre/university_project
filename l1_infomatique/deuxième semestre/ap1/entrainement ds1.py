#ds 2018-2019

#exo1

#q1
def mystere(l,n):
    for i in range(n):
        l.append(l[len(l)-1])
        for k in range(len(l) -2,0,1):
            l[k]= l[k] + l[k-1]
        print(l)



#q2
#>>> mystere(l,8)
#[1, 1]
#[1, 1, 1]
#[1, 1, 1, 1]
#[1, 1, 1, 1, 1]
#[1, 1, 1, 1, 1, 1]
#[1, 1, 1, 1, 1, 1, 1]
#[1, 1, 1, 1, 1, 1, 1, 1]
#[1, 1, 1, 1, 1, 1, 1, 1, 1]
        
#exo2

#q1
#Recherche séquentielle dans une structure non triée

#Faux ←trouve 
#i←a
#TQ non trouve et i<b
#    Si ℓ[i]=x
#    trouve ←Vrai
#Fin Si
#i←i+1
#Fin TQ
#Renvoyer : trouve


#Recherche séquentielle dans une structure triée

#i←a
#TQ i<b et x<ℓ[i]
# i←i+1
#Fin TQ
#Si i<b et x=ℓ[i]
#    Renvoyer : Vrai
#Sinon
# Renvoyer : Faux
#Fin Si

#Dans tous les cas, recherche fructueuse ou non, une recherche fastidieuse dans une tranche ℓ[a:b] coûte b−a comparaisons.

#q2
#Recherche dichotomique dans une structure triée
#d=a
#f=b-1
#tq d<f:
 #   m=(d+f)/2:
#        si compare(l[m],x)<0:
#            d=m+1
#        sinon:
#            f=m
#        fin si
#fin tq
#si x=l[d]:
#   renvoyer: Vrai
#sinon:
#    renvoyer: Faux
#fin si
            
#c(n)=1+log2n.
#contraintes= liste homogène, d'entiers

#q3
def recherche (x,l,a,b):
    """
    fonction qui renvoie si l'élement x est dans la liste l, dans l'intervalle [a,b]. Si la liste l est triée, la focntion effectue une
    recherche dichotomique, si la liste est pas triée, elle effectue une recherche sequentielle .
    :param x: (int) l'indice qu'on souhaite savoir dans la liste l, dans l'intervalle [a;b]
    :param l: (liste) une liste d'entiers
    :param a: (int) borne inf
    :param b: (int) borne sup
    :param res: (bool) retourne si vrai l'élement est dans la liste l, dans l'intervalle [a,b] ou faux dans le cas inverse 
    """
    if est_trie(l):
        res= recherche_dico(x,l,a,b)
    else:
        res= recherche_seq(x,l,a,b)
    return res
#la fonction possède est favorable, dans le sens elle limite les coûts de comparaisons

#exo4
etudiants=[{'nip':'16357914','nom':'KANE','prenom':'FABIAN','formation':'PEIP','groupe':'15'},{'nip':'12003380','nom':'DIOP','prenom':'MAXIME','formation':'MASS','groupe':'2'},
           {'nip':'16848599','nom':'ABIH','prenom':'MOHAMED','formation':'SESI','groupe':'41'},{'nip':'10283742','nom':'BURIE','prenom':'MAXENCE','formation':'SESI','groupe':'44'},
           {'nip':'19940051','nom':'IKUZA MAHIRWE','prenom':'ESTELLE','formation':'SESI','groupe':'41'}]

#q1
def dico_etudiants(numnip):
    i=0
    for carac in etudiants:
        score=etudiants[i]
        if (score["nip"])==numnip:
            mon_dict= dict(etudiants[i])
        i=i+1
    return mon_dict

#q2 
def index_etudiants(numnip):
    i=0
    for carac in etudiants:
        score=etudiants[i]
        if (score["nip"])==numnip:
            res= i
        i=i+1
    return res
    
   
#q3 à revoir 
def par_groupe(dictionnaire,formation,groupe):
    i=0
    ma_liste=list()
    for carac in dictionnaire:
        score=dictionnaire[i]
        if score['formation']==formation and score['groupe']==groupe:
            ma_liste+= [score['nip'], ]
        i=i+1
    return ma_liste
        
    

#q4
#1

#2
    

#DS 2017-2018

#exo1
#q1

def chaine_en_date(chaine):
    chaine1=chaine.split('/')
    mon_dict={"jour":chaine1[0],'mois':chaine1[1],'annee':chaine1[2]}
    return mon_dict
   
#q2
def date_en_chaine(aujourdhui):
    a=aujourdhui["jour"]
    b=aujourdhui["mois"]
    c=aujourdhui["annee"]
    return '/'.join([a, b , c])
    
    
#exo2
TABLEAU_DES_MEDAILLES={'Allemagne':[('Luge simple hommes', 'BRONZE')],
                       'Corée du Sud' : [('Short track 1500m hommes','GOLD')],
                       'Pays-Bas':[('Short track 1500m hommes','SILVER'),('Patinage de vitesse 5000m hommes', 'GOLD'),('Patinage de vitesse 3000m femmes','GOLD'),('Patinage de vitesse 3000m femmes','SILVER'),('Patinage de vitesse 3000m femmes','BRONZE')],
                       'Autriche':[('Luge simple hommes','GOLD')],'Russie':[('Short track 1500m hommes','BRONZE')],'Etats-Unis':[('Luge simple hommes','SILVER')],'Canada':[('Patinage de vitesse 5000m hommes','SILVER'),('Ski acrobatique bosses femmes','SILVER')],
                       'Norvège':[('Patinage de vitesse 5000m hommes','BRONZE')],
                       'Kazakhstan':[('Ski acrobatique bosses femmes','BRONZE')],
                       'Jamaïque':[]}
#q1
#1
def cb_pays_medailles(tableau):
    for carac in tableau:
        return len(carac)
    
#2
def nb_madailles(pays):
    return len(TABLEAU_DES_MEDAILLES[pays])

#3
def nb_medaille_niveau(pays,niveau):
    compteur=0
    i=0
    tableau=TABLEAU_DES_MEDAILLES[pays]
    for carac in tableau:
        if tableau[i][1]==niveau:
            compteur+=1
        i+=1
    return compteur
#4
def nb_medailles(tableau):
    cmp=0
    for i in tableau:
        cmp += len(tableau[i])
    return cmp

#q2
def epreuves_courues(tableau):
    liste=list()
    i=0
    liste1=list()
    for carac in tableau:
        liste+=tableau[carac]

    while i<=len(liste)-1:
        liste1+=[liste[i][0],]
        i+=1
    return set(liste1)
  
        
#q3
def ajouter_resultat(tableau,pays,sport,medaille):
    tableau.update( { pays : [(sport, medaille)]} )   #ajoute ujne clé au dictionnaire
    print(tableau)

#q4
def medailles_par_sport(tableau,sport):
    p1=""
    p2=""
    p3=""
    for i in tableau:
        for element in tableau[i]:
            if element[0]== sport and element[1]=='GOLD':
                p1=i
            elif element[0]== sport and element[1]=='SILVER':
                p2=i
            elif element[0]== sport and element[1]=='BRONZE':
                p3=i
    return (p1,p2,p3)
                
#q5 
def nombre_medailles(tableau,pays):
    gold=0
    silver=0
    bronze=0
    liste_pays=tableau[pays]
    for i in range(len(liste_pays)):
        if liste_pays[i][1]=="GOLD":
            gold=gold+1
        elif liste_pays[i][1]=="SILVER":
            silver=silver+1
        elif liste_pays[i][1]=="BRONZE":
            bronze=bronze+1
    return (gold,silver,bronze)
    
#q6 à revoir
def afficher_rang1(tableau):
    new_dict=dict()
    for carac in tableau:
        new_dict.update({carac:nombre_medailles(tableau,carac) })
    mavar = new_dict.items()
    montri = sorted(mavar, key=lambda x: x[1], reverse=True)
    [print(j, i) for i, j in montri]
        
        

#ds 2015-2016
#exo1
#q1
def est_trie(l):
    precedent = l[0]
    for element in l:
        if element < precedent:
            return False
        precedent = element
    return True

    
def kesaco(e,l):
    """
    la fonction prend en paramètre une liste l et un entier e, renvoie l'indice de l'élement e si il est dans la liste l,si e n'est pas dans la liste l, il renvoie -1.
    :param e: (int) un entier
    :param l: (list) une liste d'entiers
    :return: (int) renvoie un entier
    CU: l est une liste dont les élements sont trié dans ordre croissant, et les élements que de type int ou float
    exemple:
    >>> kesaco(12,[10,12,14,15])
    1
    >>> kesaco(5,[10,12,14,15])
    -1
    """
    assert est_trie(l)==True, "l doit être croissante"
    a=0
    b=len(l)-1
    while a<=b:
        m=(a+b)//2
        if l[m]== e:
            return m
        elif l[m]>e:
            b= m-1
        else:
            a=m+1
    return -1
    
#q2 voir le tableau
"""
>>> kesaco(5,[10,12,14,15])
-1        
>>> kesaco(12,[10,12,14,15])
1
>>> kesaco(13,[10,12,14,15])
-1
"""

#q3 faire docstring et doctests voir q1
#q4 donner des cu en plus, voir q1
            
#exo2
FILMS={'Indiana Jones et la dernière croisade':{'Harrison Ford','Sean Connery'},'Star Wars VII':{'Harrison Ford','Adam Driver'},'Frances Ha':{'GretaGerwing','Adam Driver'},
       'Star Wars III':{'Hayden Christensen','Natalie Portman','Ewan McGregor'},'Goldfinger':{'Sean Connery'},'Léon':{'Jean Réno','Natalie Portman'}}
#q1
def nb_acteurs(dictionnaire,film):
    return len(dictionnaire[film])

#q2
def filmographie(dictionnaire,acteur):
    filmographie1=list()
    for carac in dictionnaire:
        if acteur in dictionnaire[carac]:
            filmographie1+= [carac,]
    return set(filmographie1)


#q3
def ens_acteurs(dictionnaire):
    liste_acteurs=list()
    i=0
    liste=[]
    for carac in dictionnaire:
        liste_acteurs+=[dictionnaire[carac], ]
    while i<=(len(liste_acteurs)-1):
        liste+=list(liste_acteurs[i])
        i+=1
    return set(liste)

#q4
def co_acteurs(dictionnaire,acteur):
    filmographie1=list()
    for carac in dictionnaire:
        if acteur in dictionnaire[carac]:
            filmographie1+= list(dictionnaire[carac])
    f=filmographie1.count(acteur)
    for i in range(f):
        filmographie1.remove(acteur)
    return set(filmographie1)    
    
#q5
def table_acteurs(dictionnaire):
    new_dict={}
    for carac in ens_acteurs(dictionnaire):
        new_dict.update({carac: filmographie(dictionnaire,carac)})
    return new_dict

#q6 à refaire sans le max
def acteurs_populaires(dictionnaire):
    new_dict=dict()
    toto=[]
    t=table_acteurs(dictionnaire)
    for carac in t:
        new_dict.update({carac:len(t[carac])})
    for element in new_dict:
        if new_dict[element]==max(new_dict.values()):
            toto+= [element, ]
    return toto
#exo3
#q1
def echanger(l,i,j):
    l[i],l[j]=l[j],l[i]
    return (l)
def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
    
def pair_impair(l,comp=compare):
    """effectue une étape du tri pair et impair
    CU : l liste homogène d'éléments comparables selon comp
    """
    res=True
    for k in range(0,len(l)-1,2):
        if comp(l[k],l[k+1])>0:
            echanger(l,k,k+1)
            res=False
    for k in range(1,len(l)-1,2):
        if comp(l[k],l[k+1])>0:
            echanger(l,k,k+1)
            res=False
    return res
#q2 à revoir 
#>>> pair_impair([1,2,6,7,3,4,5,0],comp=compare)
#False

#q3 à revoir

#q4
#q5
#q6
#q7
                    
                
            
                
            
    



#q4
#>>> pair_impair([1,2,3,4,5],comp=compare)
#True
    
    
#ds 2014-2015
#exo1
#q1
def capitalise(m):
    """
    renvoie la chaine de caractère m mais met une majuscule au premier caractère de la chaîne de caractère.
    """
    assert type(m)==str
    if m=="":
        return ""
    else:
        return m[0].upper()+m[1:]
            
#q2
#>>> cclndjfspdm="di-".join(["lun","mar","mercre","jeu","vendre","same","dimanche"])
#>>> print(cclndjfspdm)
#lundi-mardi-mercredi-jeudi-vendredi-samedi-dimanche
#>>> type(cclndjfspdm)
#<class 'str'>
# son contenu est une chaîne de caractère, avec tout les jours de la semaine.

#q3
#jf="lundi-mardi-mercredi-jeudi-vendredi-samedi-dimanche"
#lf=jf.split("-")
#>>> print(lf)
#['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

#décompose la chaîne et ajoutes les données à une liste à l'aide d'un marqueur défini, ici '-'.

#q4
ld=["montag","dienstag","mittwoch","donnerstag","freitag","samstag","sonntag"]

jf="lundi-mardi-mercredi-jeudi-vendredi-samedi-dimanche"
lf=jf.split("-")


def majuscule_all(chaine):
    new_ld=[]
    for carac in chaine:
        new_ld+=[capitalise(carac), ]
    return new_ld
        
        
    
#q5 à apprendre
new_dict = {x:y for x,y in zip(majuscule_all(ld), lf)}
        
#q6
def ist_tag(chaine):
    if chaine in new_dict.keys():
        return True
    else:
        return False
   
#q7
def traduction_jour(jour):
    if jour in new_dict.keys():
        return new_dict[jour]
    else:
        print("il y a erreur, ce jour n'existe pas")

#q8 à apprendre
def inverse(dictionnaire):
    reversed_dict ={v: k for k, v in dictionnaire.items()}
    return reversed_dict
    
#exo3
#q1
etudiants={1123211:{'nom':'Calbuth','prénom':'Raymond'},
           1123212:{'nom':'Cru','prénom':'Carmen'},
           1123213:{'nom':'Talon','prénom':'Achille'}}
es={405678:{'UE':'Info','Intitulé':'Informatique','coeff':4},
    405679:{'UE':'AP1','Intitulé':'Algorithmes et Programmation 1','coeff':5}}
notes={(1123211,405678):12.5,
       (1123212,405679):13.0,
       (1123212,405678):14.5,
       (1123213,405679):15.5,
       (1123213,405678):18.5}
#q1
#il manque une note à l'élève 1123211, Calbuth Raymond, celle d'ap1.
#q2
def listenotes(nipetudiant):
    l=[]
    for e,u in notes:
        if e==nipetudiant:
            l.append(notes[(e,u)])
    return l


#>>> listenotes(1123212)
#[13.0, 14.5]

#q3
def couple(nipetudiant):
    l=[]
    for e,u in notes:
        if e==nipetudiant:
            l.append(u)
            l.append(notes[(e,u)])            
    return l
   
#q4
def moyenne_generale(nipetudiant):
    d=listenotes(nipetudiant)
    if len(listenotes(nipetudiant))<2:
        print("None")
    else:
        d=(d[0]+d[1])/2
    return d


        
#q5
def bulletin(nip):
    print("Nom:",etudiants[nip]['nom'],"Prénom:",etudiants[nip]['prénom'],"NIP:",nip)
    if len(couple(nip))==2:
        print(couple(nip)[0],"Info 5", couple(nip)[1])
        print("Moyenne générale:",couple(nip)[1])
    else:
        print(couple(nip)[2],"Info 5", couple(nip)[3])
        print(couple(nip)[0],"Info 5", couple(nip)[1])
        print("Moyenne générale:",moyenne_generale(nip))
        
    
#exo4
#q1
def suite_valide(l):
    i=0
    while i<=len(l)-1:
        d=l[i]
        if d[len(d) - 1]==l[i+1][0]:
            return True
            i=+1
        else:
            return False


        
        
    
    
        
        
        

            
        
            
