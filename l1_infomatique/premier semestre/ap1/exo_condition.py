#lesaffre maeva
#TP 4 exercice sur les conditions

from random import randint

#Exercice 1
#Q1
def est_dans1(x):
    
    return -1<=x and x <=3

def est_dans2(x):
    
    return -1<x and x <=3

def est_dans3(x):
    
    return (-1<x and x <=3) or (8<=x and x<10 )

def est_dans4(x):
    
    return (-1<x and x <=3) or (8<=x )

#Q2
def est_positif(nb):
    return nb>=0

def meme_signe(nb1,nb2):
    return (nb1>=0 and nb2>=0) or (nb1<=0 and nb2<=0)

#Q3
def dans_rectangle(x,y):
    return (x>=2 and x<=10) and (y>=4 and y<=8)

def dans_disque(x,y):
    return (x-6)**2 +(y-4)**2 <= 4 
    
#Q4 
def est_pair(nb):
    return nb%2 == 0

def yacoupe(nb):
    return (nb>=1930 and nb<1942 or nb>1946 ) and (nb-1930)%4 == 0


#Exercise 2
#Q1
def  maximum(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return a

def minimum(a,b):
    if a<b:
        return a
    elif b<a:
        return b
    else:
        return a

def valeur_absolue(a):
    if a>=0:
        return a
    else:
        return -a
    
def pile_ou_face():
    p = randint(0,1)
    if p == 0:
        return "head"
    else:
        return "tail"
    
#Exercise 3 
def cle(gp):
    gp = str(gp)
    psw = input("What is the password ?")
    if psw == "info_17-18_"+gp:
        print("Welcom to",gp)
    else:
        print("Invalid passcode!")

#Exercise 4
def est_rectangle(a,b,c,error):
    return (c**2 == a**2+b**2 or a**2 == c**2+b**2 or b**2 == a**2+c**2) and ( (a**2 +b**2- error <= c**2 and a**2 +b**2- error <= c**2) or (c**2 +b**2- error <= a**2 and c**2 +b**2- error <= a**2) or (c**2 +a**2- error <= b**2 and c**2 +a**2- error <= b**2)  )
    
#Exercise 5
def est_perime(d,m,y,de,me,ye):
    return y>ye or  ( y == ye and m>me )or ( y == ye and m == me and d>=de)