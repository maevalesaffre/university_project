
#exo1
#q1
"""
>>> mon_tuple=(5, 8, 6, 9)
>>> a=mon_tuple[1]
>>> print (a)
8
"""
#q2
def somme(t):
    """
    calcule la somme des éléments de un tuple passée en paramètre.
    :param t: (tuple) tuple
    :return s:(int) un entier
    :CU: tout les élements du tuple sont des entiers
    :exemples:
    >>> somme(())
    0
    >>> somme((6,7,8))
    21
    
    """
    s= 0
    for i in range(len(t)):
        s= s + t[i]
    return
#q3
def compte(t):
    s=0
    for i in range(len(t)):
        if t[i]=="o":
            s+=1
    return s