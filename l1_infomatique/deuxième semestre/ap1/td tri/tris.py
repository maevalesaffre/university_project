from functools import cmp_to_key
import functools
#exo1
#q1
def compare_date(d1,d2):
    if d1["années"]<d2["années"]:
        return -1
    elif d1["années"]>d2["années"]:
        return 1
    elif d1["mois"]<d2["mois"]:
        return -1
    elif d1["mois"]>d2["mois"]:
        return 1
    elif d1["jours"]<d2["jours"]:
        return -1
    elif d1["jours"]>d2["jours"]:
        return 1
    else:
        return 0
    

etudiants = [(99998132,"Calbuth","Raymond",{"jour":12,"mois":12,"annee":1987}),
               (99994451,"Talon","Achille",{"jour":7,"mois":11,"annee":1963}),
               (99996348,"Calbuth","Monique",{"jour":29,"mois":7,"annee":1987}),
               (99995433,"Blanc-Sec","Adèle",{"jour":17,"mois":4,"annee":1976}),
               (99997674,"Brisefer","Benoît",{"jour":15,"mois":12,"annee":1960}),
               (99998324,"Lagaffe","Gaston",{"jour":28,"mois":2,"annee":1957})]


#q2
def classer_nip(classement):
    classement.sort()
    for etu in classement:
        print(etu[1],etu[2])
        
#q3
def classer_nip_inverser(classement):
    classement.sort(reverse=True)
    for etu in classement:
        print(etu[1],etu[2])
        
#q4

#q5    
def classer_age_croissant(classement):
    classement.sort (key = cmp_to_key (compare_age_etudiants))
    for etu in classement:
        print(etu[1],etu[2])
        
#ex2
#q1
LETTRES = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
def compare_car(c1,c2):
    if c1 in LETTRES and c2 in LETTRES:
        return compare_num (LETTRES.index (c1), LETTRES.index (c2))
    elif c1 in LETTRES:
        return -1
    elif c2 in LETTRES:
        return 1
    else:
        return compare_num (ord (c1), ord (c2))

#q2
def compare_chaine (ch1, ch2):
    lg1 = len (ch1)
    lg2 = len (ch2)
    comp_long = compare_num (lg1, lg2)
    if comp_long != 0:
        return comp_long
    else:
        i = 0
        meme_car = True
        while i < lg1 and meme_car:
            meme_car = ch1[i] == ch2[i]
            if meme_car: i += 1
            # (i == lg1 et ch1 == ch2) ou (meme_car != True et ch1[i] != ch2[i])
            if i == lg1:
                return 0
            else:
                return compare_car (ch1[i], ch2[i])

#q3
def est_trie (l, comp):
    n = len (l)
    i = 0
    while i < n - 1 and comp(l[i],l[i+1]) <= 0:
        i += 1
    return i == n- 1

