#comment
import struct
from struct import *
import time
from math import *


# un triangle est un tuple (liste ? ) de trois sommets
# un sommet est une liste de trois flottants
# un plan est une liste (tuple ? ) de 4 coefficients ax+by+cz+d=0
# On s'occupe seulement des plans parallèles aux axes
# exemple -> ax+d=0 : plan perpendiculaire à l'axe ox passant par le point (-d/a,0,0)
# deux points sont sur des faces opposées d'un plan si l'équation du plan pour
# chacun est de signe opposé.

# Version 2 :
# a) On fait des fonctions plutot que du code tout mélangé
# b) on isole les contours fermés pour simplifier le boulot de la découpeuse laser.

# Version 3 :
# Pour la réalisation pratique :
# - Plexi 3mm, cube 12cm de coté -->40 plaques
# A priori en deux fichiers (necessite des plaques 60cmx48cm minimum)
# les tranches sont réparties sur deux fichiers
# la mise à l'échelle sera faite à l'exterieur du programme


bornesX=[0.0,0.0]
bornesY=[0.0,0.0]
bornesZ=[0.0,0.0]

def lireFile(nom):
    """
    lire les triangles dans le fichier stl
    retourne une liste de triangles (triplets de positions des sommets)
    On repere aussi les bornes de l'objets dans les trois dimensions (bornes_) 
    """
    
    fichier=open(nom,"rb")
    # Les 80 premiers octets sont un commentaire
    comment=fichier.read(80)
    print(comment)
    # lire le nombre de triangles (entier sur 4 octets)
    nbT=fichier.read(4)
    nbTriangles=int.from_bytes(nbT,byteorder='little')
    print('nombre de triangles : {0:d} '.format(nbTriangles))
    # en fait, une bete liste sans indexation suffirait
    triangles=[[(0.0,0.0,0.0) for i in range(3)] for j in range(nbTriangles)]
    
    
    
    for i in range(nbTriangles):
        # Lire chaque triangle ( 4 flottants sur 32 bits + un entier de controle)
        for j in range(4):
            values=[0.0,0.0,0.0]
            # lire les 4 flottants (le premier est sans interet)
            for k in range(3):
             # Lire 4 octets dans le fichier
             val=fichier.read(4)
             # interpreter les 4 octets comme étant un flottant en little endian
             values[k]=struct.unpack('f',val)[0]
            #print(values)
             # trouver les bornes de l'objets dans les trois dimensions
             if(j!=0):
                 if(values[0]<bornesX[0]): bornesX[0]=values[0]
                 if(values[0]>bornesX[1]): bornesX[1]=values[0]

                 if(values[1]<bornesY[0]): bornesY[0]=values[1]
                 if(values[1]>bornesY[1]): bornesY[1]=values[1]

                 if(values[2]<bornesZ[0]): bornesZ[0]=values[2]
                 if(values[2]>bornesZ[1]): bornesZ[1]=values[2]
                 
                 triangles[i][j-1]=values
        # lecture et oubli de l'entier de controle         
        fichier.read(2)
    return triangles


def position(point,plan):
    """
    position d'un point par rapport à un plan
    """
    
    vx=point[0]
    vy=point[1]
    vz=point[2]
    cpa=plan[0]
    cpb=plan[1]
    cpc=plan[2]
    cpd=plan[3]
    return cpa*vx+cpb*vy+cpc*vz+cpd

def signe(valeur):
    return valeur>=0

def estCoupe(triangle,plan):
    """
    vaut vrai si le triangle est coupé par le plan
    """
    
    v1=position(triangle[0],plan)
    v2=position(triangle[1],plan)
    v3=position(triangle[2],plan)
    #print(v1,",",v2,",",v3)
    return((signe(v1)!=signe(v2))or(signe(v1)!=signe(v3))or(signe(v2)!=signe(v3)))

def imprimeTriangle(t):
    print("\t",t[0])
    print("\t",t[1])
    print("\t",t[2])

def decoupe(triangle,plan):
    """
    retourne les deux extremites du segment du triangle coupe par le plan
    """
    assert estCoupe(triangle,plan), "le triangle n'est pas coupe par le plan"
    if(signe(position(triangle[0],plan))==signe(position(triangle[1],plan))):
       rebelle=2
       ami1=0
       ami2=1
    if(signe(position(triangle[0],plan))==signe(position(triangle[2],plan))):
       rebelle=1
       ami1=0
       ami2=2
    if(signe(position(triangle[1],plan))==signe(position(triangle[2],plan))):
       rebelle=0
       ami1=1
       ami2=2
    # calculer le point entre rebelle et ami1
    moulin=triangle[rebelle]
    lacombe=triangle[ami1]
    d1=position(moulin,plan)
    d2=position(lacombe,plan)
    denom=d2-d1
    alpha=d2/denom
    inter1=[moulin[i]*alpha for i in range(3)]
    inter2=[lacombe[i]*(1-alpha) for i in range(3)]
    extreme1= [inter1[i]+inter2[i] for i in range(3)]
    # deuxieme extremite
    lacombe=triangle[ami2]
    #d1=position(moulin)
    d2=position(lacombe,plan)
    denom=d2-d1
    alpha=d2/denom
    inter1=[moulin[i]*alpha for i in range(3)]
    inter2=[lacombe[i]*(1-alpha) for i in range(3)]
    extreme2= [inter1[i]+inter2[i] for i in range(3)]
    return[extreme1,extreme2]   
       
def distance(x,y):
    dx=(x[0]-y[0])*(x[0]-y[0])
    dy=(x[1]-y[1])*(x[1]-y[1])
    dz=(x[2]-y[2])*(x[2]-y[2])
    return sqrt(dx+dy+dz)
    
    
        

def notend(seg):
    if abs(seg[0][0])>=28.99:
        return False
    if abs(seg[1][0])>=28.99:
        return False
    if abs(seg[0][2])>=28.99:
        return False
    if abs(seg[1][2])>=28.99:
        return False
    return True


"""
def notend(seg):
    return True
"""

def calculcouches(nbSteps):
    """
    Fabrique toutes les tranches découpées dans l'objet
    Chaque couche est une liste de segments,
    chaque segment est l'intersection d'un triangle de l'objet avec
    le plan de coupe.
    """
   
    #epaisseur des tranches
    step=(bornesY[1]-bornesY[0])/(2*nbSteps)
    couches=[]
    for i in range(nbSteps+2):
        minSegX=1000
        maxSegX=0
        minSegZ=1000
        maxSegZ=0
        print("tranche numero ",i)
        # calcul des segments d'une tranche
        laCouche=[]
        lePlan=[0,1,0,-(bornesY[0]+(2*i-1)*step)]
        lesTrianglesCoupes=[ t for t in lesTriangles if estCoupe(t,lePlan)]
        #for t in lesTrianglesCoupes:
         #imprimeTriangle(t)
         #print()
        print(len(lesTrianglesCoupes),",",(bornesY[0]+i*step))
        for t in lesTrianglesCoupes:
           segment=decoupe(t,lePlan)
           if(segment[0][0]<minSegX):
               minSegX=segment[0][0]
           if(segment[1][0]<minSegX):
               minSegX=segment[1][0]
           if(segment[0][0]>maxSegX):
               maxSegX=segment[0][0]
           if(segment[1][0]>maxSegX):
               maxSegX=segment[1][0]

           if(segment[0][2]<minSegZ):
               minSegZ=segment[0][2]
           if(segment[1][2]<minSegZ):
               minSegZ=segment[1][2]
           if(segment[0][2]>maxSegZ):
               maxSegZ=segment[0][2]
           if(segment[1][2]>maxSegZ):
               maxSegZ=segment[1][2]
           
           #print((bornesY[0]+i*step)," ",segment[0],"**",segment[1])
           if notend(segment):    
            laCouche.append(segment)
        couches.append(laCouche)
        print(minSegX," ",maxSegX," ",minSegZ," ",maxSegZ)
        print(maxSegX-minSegX," ",maxSegZ-minSegZ)

    return couches
    # fin de découpe tranches

def regroupe(couche):
    """
    Pour une couche donnée (i.e. une liste de segments (couples d'extremites)
    regrouper dans l'ordre tous les segments qui forment une suite (idéalement une
    courbe fermee
    """
    # Liste des classes d'equivalence
    # (On suppose qu'il n'y a pas de T ou de croix dans la coupe)
    courbes=[]
    couchecopy=couche.copy()
    print("nombre de segments ",len(couche))
    while len(couchecopy)!=0:
        # prendre une graine et construire la courbe dont elle est le départ
        section=[couchecopy.pop()]
        possible=True
        while possible:
            possible=False
            for i in range(len(couchecopy)):
                if couchecopy[i][0]==section[-1][1]:
                    possible=True
                    value=couchecopy[i]
                    section.append(value)
                    couchecopy=couchecopy[:i-1]+couchecopy[i+1:]
                    break
                    
                if couchecopy[i][1]==section[-1][1]:
                    possible=True
                    value=couchecopy[i]
                    value.reverse()
                    section.append(value)
                    couchecopy=couchecopy[:i-1]+couchecopy[i+1:]
                    break
               
                if couchecopy[i][0]==section[0][1]:
                    possible=True
                    value=couchecopy[i]
                    value.reverse()
                    section=[value]+section
                    couchecopy=couchecopy[:i-1]+couchecopy[i+1:]
                    break
                    
                if couchecopy[i][1]==section[0][1]:
                    possible=True
                    value=couchecopy[i]
                    section=[value]+section
                    couchecopy=couchecopy[:i-1]+couchecopy[i+1:]
                    break
 
            courbes.append(section)
    return courbes

def construitligne(listeencours,vivier):
    """
    liste en cours contient les points ordonnes constituant la ligne
    deja construite.
    Au départ, on y met les deux extremites d'un segment
    Ensuite, on va chercher dans vivier si un point peut se recoller
    à droite ou à gauche
    """
    igauche=-1
    idroite=-1
    cgauche=[]
    cdroite=[]
    trouve=False
    for i in range(len(vivier)):
        candidat=vivier[i]
        # chercher s'il colle a gauche
        #if candidat[0]==listeencours[0]:
        if distance(candidat[0],listeencours[0])<1e-6:
            cgauche=[candidat[1]]
            igauche=i
        #if candidat[1]==listeencours[0]:
        if distance(candidat[1],listeencours[0])<1e-6:
            cgauche=[candidat[0]]
            igauche=i
        #chercher s'il colle à droite
        #if candidat[0]==listeencours[-1]:
        if distance(candidat[0],listeencours[-1])<1e-6:
            cdroite=[candidat[1]]
            idroite=i
        #if candidat[1]==listeencours[-1]:
        if distance(candidat[1],listeencours[-1])<1e-6:
            cdroite=[candidat[0]]
            idroite=i
    listeencours=cgauche+listeencours+cdroite
    newvivier=[]
    for i in range(len(vivier)):
        if(i!=igauche) and (i!=idroite):
            newvivier.append(vivier[i])
        else:
            trouve=True
    #print(i," ",igauche," ",idroite," ",candidat)
    return listeencours,newvivier,trouve

def construitcourbes(couche):
    """
    Pour une couche de decoupe, cherche toutes les courbes continues
    On prend un segment, on utilise la fonction construitligne qui le prolonge
    au maximum, puis on revient avec les points qui restent
    """
    provi=couche.copy()
    lescourbes=[]
    while len(provi)!=0:
        k=provi.pop()
        ligneencours=[k[0],k[1]]
        ligneencours,provi,trouve=construitligne(ligneencours,provi)
        while(trouve):
             ligneencours,provi,trouve=construitligne(ligneencours,provi)
        lescourbes.append(ligneencours)
    return lescourbes
            
            
            
    
    

def polyligneSVG(suite,transform="",couleur="red"):
    s="<polygon fill=\"none\" stroke=\""+couleur+"\"\n points=\" "
   
    for i in range(len(suite)):
        d0=COEFA*suite[i][0]+COEFB
        f0=COEFA*suite[i][2]+COEFB
        s=s+str(d0)+","+str(f0)+" "
    s=s+"\" transform="+transform+" />\n"
    return s

def cercleSVG(x,y,r,transform="",couleur="red"):
    s="<circle cx=\""+str(x)+"\" cy=\" "+str(y)+"\" r=\" "+str(r)+"\" fill =\"none\" stroke=\""+couleur+"\"   transform="+transform+" />\n"
    return s


def ligneSVG(debut,fin,transform="",color="red"):
     d0=COEFA*debut[0]+COEFB
     d1=COEFA*debut[2]+COEFB
     f0=COEFA*fin[0]+COEFB
     f1=COEFA*fin[2]+COEFB
     
     s="<line x1=\""+str(d0)+"\" y1=\""+str(d1)+"\" x2=\""+str(f0)+"\" y2=\""+str(f1)+"\" stroke=\""+color+"\"   transform="+transform+" />\n"
     return s

def ligneSVGpure(debut,fin,transform="",color="red"):
     s="<line x1=\""+str(debut[0])+"\" y1=\""+str(debut[1])+"\" x2=\""+str(fin[0])+"\" y2=\""+str(fin[1])+"\" stroke=\""+color+"\"   transform="+transform+" />\n"
     return s
    
def decalage(n):
    return "\"translate("+str((CARRE)*(n//COLONNES))+","+str((CARRE)*(n%COLONNES))+")\""
def decalagebis(n):
    #return "\"translate("+str((CARRE)*(n//COLONNES))+","+str((CARRE)*(n%COLONNES))+20")\""
    return "\"translate("+str((CARRE)*(n//COLONNES))+","+str((CARRE)*(n%COLONNES))+")\""

if __name__=="__main__":
    print("debut")
    lesTriangles=lireFile("plexicreux.stl")
    
    # Prevoir deux carrés en plus, pour etre sûr d'avoir des faces sans trous aux extremités.
    LIGNES=5
    COLONNES=4
    couches=calculcouches(36)
    print(len(couches))

    print(bornesX)
    print(bornesY)
    print(bornesZ)

    LARGEUR=500
    HAUTEUR=LARGEUR



    entete="<svg viewBox=\"0 0 "+str(5000)+" "+str(5000)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    decoupe1=open("plexiplaque1.svg","w")
    decoupe2=open("plexiplaque2.svg","w")
    decoupe1.write(entete)
    decoupe2.write(entete)
   
    CARRE=500 # pareil que largeur

    # Un truc approximatif pour centrer l'objet dans le cadre
    # A revoir....
    ExpandX=bornesX[1]-bornesX[0]
    ExpandY=bornesY[1]-bornesY[0]
    ExpandZ=bornesZ[1]-bornesZ[0]

    # essai de centrage de l'image

    print("expansion X ",ExpandX,bornesX)
    print("expansion Y ",ExpandY,bornesY)
    print("expansion Z ",ExpandZ,bornesZ)


    if ExpandX>ExpandZ:
        EMPAN=bornesX
    else:
        EMPAN=bornesZ
    COEFA=(LARGEUR-1)/(EMPAN[1]-EMPAN[0])
    COEFB=-EMPAN[0]*COEFA

    i=0
    j=0
   
    colors=["red","blue","green","black"]
    diam=7.9
    for c in couches:
         u=construitcourbes(c)
         print(i," ",len(c))
         if i<20:
             tfm=decalage(i)
         else:
             tfm=decalage(i-20)
         if i<20:
             decoupe1.write(cercleSVG(20,20,diam,transform=tfm))
             decoupe1.write(cercleSVG(20,480,diam,transform=tfm))
             decoupe1.write(cercleSVG(480,20,diam,transform=tfm))
             decoupe1.write(cercleSVG(480,480,diam,transform=tfm))
         else:
             decoupe2.write(cercleSVG(20,20,diam,transform=tfm))
             decoupe2.write(cercleSVG(20,480,diam,transform=tfm))
             decoupe2.write(cercleSVG(480,20,diam,transform=tfm))
             decoupe2.write(cercleSVG(480,480,diam,transform=tfm))
             
         for serpent in u :
             if(i<20):
              #decoupe1.write(polyligneSVG(serpent,transform=tfm,couleur=colors[j%len(colors)]))
              decoupe1.write(polyligneSVG(serpent,transform=tfm))
             else :
              #decoupe2.write(polyligneSVG(serpent,transform=tfm,couleur=colors[j%len(colors)]))
              decoupe2.write(polyligneSVG(serpent,transform=tfm))
             j=j+1
         i=i+1
    for l in range(0,LIGNES+1):
        decoupe1.write(ligneSVGpure((CARRE*l,0),(CARRE*l,CARRE*COLONNES)))
        decoupe2.write(ligneSVGpure((CARRE*l,0),(CARRE*l,CARRE*COLONNES)))

    for l in range(0,COLONNES+1):
        decoupe1.write(ligneSVGpure((0,CARRE*l),(CARRE*LIGNES,CARRE*l)))
        decoupe2.write(ligneSVGpure((0,CARRE*l),(CARRE*LIGNES,CARRE*l)))
    
         
         
    decoupe1.write(pied)
    decoupe1.close()
    decoupe2.write(pied)
    decoupe2.close()
   

    
