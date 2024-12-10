#exo1
#q1
protection={'.':"[dot]", '@':"[at]"}

#q2
def transforme(chaine,dictionnaire):
    rep=""
    for c in chaine:
        if c in dictionnaire.keys():
            rep+= dictionnaire[c]
        else:
            rep+= c
    return rep
            
#q3
def protege_adresse(chaine):
    rep=""
    for carac in chaine:
        if carac in protection.keys():
            rep+= protection[carac]
        else:
            rep+= carac
    return rep
            
#q4
def inverse_dico(d):
    d_fin={}
    i=0
    val=list(d.values())
    keys=list(d.keys())
    for elt in val:
        d_fin[elt]=keys[i]
        i+=1
    return d_fin
#q5
def deprotege_adresse():
    rep=""
    for carac in chaine:
        if carac in protection.keys():
            rep+= protection[carac]
        else:
            rep+= carac
    return rep
    
    
            
    
    
    