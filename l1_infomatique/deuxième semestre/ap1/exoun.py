#exo1
a=[(3,1),(4,1),(5,9)]
#q1
#>>> a[1][0]
#4

#q2
#a[2][1]

#q3
#a=a+[(2,6)]

#q4
#a=a.pop()

#q5
def fonc(a):
    t=tuple()
    for carac in a:
        t=t+carac
    return t

#q6
#[list(element]for element in a]


#q7
#tuple(list(element)for element in a)



#exo2
a=[3,1,6,1,5,9,2]
#q1
#a[2]=4
#[3,1,4,1,5,9,2]

#q2
#a[7]
#erreur

#q3
#a.append(6)
#erreur

#q4




#a.append([6])
#a=[3,1,6,1,5,9,2,6]

#q6
def fonc2(a,b,c):
    b=a
    c=a
    b=b+[1,2,3,4]
    c.append(1)
    return a,b,c


#exo3
#q1
def fst(x):
    return x[0]

# >>> fst([1,2,3])
#1

#>>> fst("abc")
#'a'

#>>> fst(3.0)
#erreur

#>>> fst(1,2)
#erreur

#>>> fst((1,2))
#1

#>>> fst(((1,2)))
#1

#>>> fst(((1,2),))
#(1, 2)

#>>> fst([])
#erreur
 
#q2 si x est une chaîne dde caractère, une liste un ou plusieurs elements.

#exo4
#q1
def zap(couple):
    assert tuple(couple)==tuple,"le paramètre doit être un tuple"
    assert len(couple)==2, "le paramètre doit être un couple"
    assert type(couple[0])==list and type(couple[1])==list,"les 2 nembres du couples doivent être des listes"
    assert (couple[0])==len(couple[1]),"les 2 listes doivent avoir la même longueur"
    l1=couple[0]
    l2=couple[1]
    l=[]
    for i in range(len(l1)):
        l=l+[(l1[i],l2[i])]
    return l

#q2
def unzap(l):
    assert type(l)==list,"param=liste"
    l1=[]
    l2=[]
    for element in l:
        assert type(element)==tuple, "param=liste"
        assert len (element)==2, "param=liste"
        l1.append(element[0])
        l2.append(element[1])
    return l1,l2

    
#exo5
def nbocc(c):
    l=[]
    for carac in c:
        l=l+[(carac,c.count(carac))]
        
    return l
        
def nbocc_v2(c):
    l=[]
    for carac in c:
        i=0
        trouve=False
        while i<len(l) and not trouve:
            if carac==l[i][0]:
                trouve=True
            else:
                i=i+1
        if trouve:
            l[i]=(carac,l[i][1]+1)
        else:
            l.append((carac,1))
    return l
#exo6
def perm_circ_raymond(l):
    for i in range(1,len(l)):
        l[i]=l[i-1]
        l[i-1]=l[i]
    return l

#q1
#>>> perm_circ_raymond([1,2,3,4])
#[1, 1, 1]

#q2
def perm_circ_raymond_v2(l):
    l.insert(0,l.pop())
    return l

def perm_circ_raymond_v3(l):
    for i in range(1,len(l)):
        d=l[i]
        l[i]=l[i-1]
        l[i-1]=d
    return l
    