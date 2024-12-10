
#exo2
#q1
from turtle import *

#q2
def carre(l):
    for i in range(4):
        forward (l)
        left(90)

#Q3
def dessin():
    a=5
    while(a<400):
        carre(a)
        penup()
        left(30)
        forward(10)
        pendown()
        a=a+15
    return 