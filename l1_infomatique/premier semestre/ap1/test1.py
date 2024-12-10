from random import randint

def pile_face():
    x=randint(1,2)
    if x==1:
        return "pile"
    else:
        return "face"
    print(x)
