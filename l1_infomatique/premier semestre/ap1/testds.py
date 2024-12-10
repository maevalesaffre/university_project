from random import randint

def u_terme(n):
    cpt=0
    u_n=0
    while (cpt < n):
        assert n>=0, "n doit être positif ou nul"
        u_n = 1+ (10 * u_n) + (u_n % 10)
        cpt = cpt+1
    return u_n

def gainv1(m,r1,r2,r3):
    if r1==1 and r2==1 and r3==1:
        somme= m*250
    elif r1==2 and r2==2 and r3==2:
        somme= m*150
    elif r1==1 and r2==1 and r3!=1:
        somme= m*5
    elif r1==1 and r2!=1 and r3!=1:
        somme= m*2
    else:
        somme= 0
    return somme

def unité(n):
    resu=n%10
    return resu

def fonction(n):
    a = n//10
    return unité(a)

def centainev1(n):
    b = n//100
    return unité(b)

def est_nbre_amstrong(n):
    n1=unité(n)
    n2=fonction(n)
    n3=centainev1(n)
    if n3**3+n2**3+n1**3==n:
        return True
    else:
        return False

def imprimer_amstrong(m):
    for i in range(1,m+1):
        if est_nbre_amstrong(i):
            print(i)
    
def est_manque(nb):
    if 1<=nb<=18:
        return True
    else:
        return False
    
def est_impaire(nb):
    if nb%2==0:
        return False
    else:
        return True
def lance():
    x=randint(0,36)
    return x
def demande_mise():
    g=input("Quelle est votre mise? :" )
    return int(g)
def demande_case():
    h=input("sur qelle case voulez vous miser? :")
    return (h)
        
    
def montantMensualite(capital,tauxAn,nbAn):
    tauxMois = ((1+tauxAn)**(1/12))-1
    mensualite= (capital*tauxMois)/(1-(1/((1+tauxMois)**((12)*nbAn))))
    return mensualite
    
def accepteEmprunt(mensualite,salaire):
    revenuRestant = salaire-(salaire*0.03)-mensualite
    tauxEndettement = mensualite/salaire
    if tauxEndettement<= 33 and revenuRestant>600:
        return True
    elif 33<tauxEndettement<40 and revenuRestant>1500:
        return True
    else:
        return False
    
def reponseBanquier(capital,tauxAn,nbAn,salaire):
    montantMensualite(capital,tauxAn,nbAn)
    accepteEmprunt(montantMensualite(capital,tauxAn,nbAn),salaire)
    if accepteEmprunt(montantMensualite(capital,tauxAn,nbAn),salaire) == True:
        print ("Une mensualité de" ,montantMensualite(capital,tauxAn,nbAn), "est acceptée avec votre salaire")
    else:
        print ("Une mensualité de" ,montantMensualite(capital,tauxAn,nbAn), "est refusée avec votre salaire")
    
    
def dynastie(annee):
    if 481<=annee<=751:
        return 'Mérovingiens'
    elif 551<=annee<=987:
        return 'Carolingiens'
    else:
        return 'Capétiens'

def affiche_dynastie():
    g = randint(481,1792)
    if 481<= g <=751:
        return "les Mérovingiens ont régné en",g
    elif 551<=g<=987:
        return "les Carolingiens ont régné en",g
    else:
        return "les Capétiens ont régné en",g
    
    
    
    
    
    
        
    
    
    