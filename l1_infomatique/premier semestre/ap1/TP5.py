#Melanie Bulois
#Maeva Lesaffre
from turtle import *
from random import randint


#Q1
def carre(l):
    forward(l)
    left(90)
    forward(l)
    left(90)
    forward(l)
    left(90)
    forward(l)
    left(90)
    forward(l)
    
#Q2
def carre_nb(nb,l):
    for carac in range(0,nb):
         carre(l)
         penup()
         forward(5)
         pendown()
         

         

#Q3
def ligne(l):
    for carac in range(10):
        carre(l)
        penup()
        forward(l+5)
        pendown()
    
         
def carre_de_carre(l):
    speed(0)
    x = -200
    y = 300
    penup()
    goto(x,y)
    pendown()
    speed(0)
    for i in range(1,11):
        for j in range(10):
            carre(l)
            penup()
            forward(5)
            pendown()
        s = (l+5)*i
        penup()
        goto(x,y-s)
        pendown()
#Q4    
def cal():
    speed(0)
    l=10
    x = 1
    y = 1
    penup()
    goto(x,y)
    pendown()
    speed(0)
    for i in range(0,51):
        carre(l+10*i)
        s = (l+5)*i
        penup()
        goto(x,y-s)
        pendown()
#Q5 a finaliser
def carre_tournant(n):
    angle=360/n
    for carac in range(1,n+1):
        carre(100)
        left(angle)

#Cas des polygones convexes
#Q1
#Pour un polygone régulier avec n côté l'angle est de 360/n
 
#Q2
def polygone_reg_convexe(n,l):
    a=360/n
    for carac in range(n):
        forward(l)
        left(a)
#Q3        
"""pu()
goto(-100,100)
pd()
polygone_reg_convexe(4,50)
pu()
goto(100,100)
pd()
polygone_reg_convexe(5,50)
pu()
goto(-100,-100)
pd()
polygone_reg_convexe(6,50)
pu()
goto(100,-100)
pd()
polygone_reg_convexe(7,50)
"""

#Cas des polygones étoilés
#Q1
def polygone_etoile(n,l,k):
    a=(360/n*k)
    for carac in range(n):
        forward(l)
        right(a)
        
#Q2
        """
penup()
goto(-100,100)
pendown()
polygone_etoile(5,100,2)
penup()
goto(100,100)
pendown()
polygone_etoile(7,100,3)
penup()
goto(-100,-100)
pendown()
polygone_etoile(8,100,3)
penup()
goto(50,-20)
pendown()
polygone_etoile(9,100,4)
"""
        
#Q3
        """
polygone_etoile(6,100,2)
polygone_etoile(6,100,3)
polygone_etoile(6,100,4)"""

# Non, on n'obtient que des triangles equilateraux

#Mouvement brownien
#Q1
def tortue_sortie(l):
    return abs(xcor()) >=(l/2) or abs(ycor()) >= (l/2)

#Q2
def brownie():
    clearscreen()
    penup()
    goto(-200,-200)
    pendown()
    carre(400)
    penup()
    goto(0,0)
    pendown()
    while not tortue_sortie(400):
        a=randint(0,359)
        l=randint(10,30)
        right(a)
        forward(l)


def billard(Bx,By,x,y,a,bande):   
    clearscreen()
    penup()
    goto(-(Bx/2),-(By/2))
    pendown()    
    forward(Bx)
    left(90)
    forward(By)
    left(90)
    forward(Bx)
    left(90)
    forward(By)
    left(90)
    penup()
    goto(x,y)
    pendown()
    a = a % 180   
    left(a)   
    for i in range(0,bande):
        while not (abs(xcor()) >(Bx/2) or abs(ycor()) > (By/2) ):
            forward(1)
        angle = heading()%180
        if angle <90:
            left(180-90-angle)
    
            

    
    
        

        
        
    
    
    
    
    
    
    
    
        
        
        