#exo1
#q1, type=ensemble, set
#q2 len(ens)
#q3 element in s
#q4 list(ens), cette liste ne sera pas ordonnée
#q5 set('aeiou')
#q6 ens.intersection(set('aeiou')), ens.union(set('aeiou'))
#q7 set(texte) len(set(texte))
#q8 len(set(texte)).intersection(set('aeiou'))

#exo2
#q1  d[k]
#q2 d[k]=v
#q3 d[k]=v
#q4 d.pop(k)
#q5 d.keys()
#q6 d.values()
#q7 for k in d.keys():
#     print(k,'',d[k])
#q8 for k in d.keys():
#       d[k]=None
# ou  dict((k,None) for k in d.keys())


#q3
liste_mois=['janvier','février','mars','avril','mai','juin','juillet','août','semptembre','octobre','novembre','décembre']
def veille(d):
    if d['jours']!=1:
        return creer_date(['jours']-1,d['mois'],d['année'])
    if d['mois']!=1:
        return creer_date(duree_mois(d['mois']-1,d['année']),d['mois']-1,d['année'])
    
#exo4
#q1
def moyenne(a):
    L=list(a)
    for carac in L:
        carac['chimie']