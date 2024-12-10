from datalayer import DataLayer
from db_config import get_db_parms
from table_util import table_to_str


    
dl = DataLayer(**get_db_parms())

print('liste des équipes')
equipes = dl.equipes()
print(table_to_str(equipes)) 

print('liste des noms d\'étapes')
for nom in dl.liste_noms_etapes() :
    print(nom)
print()

nom = input('Recherche d\'un coureur nommé ? ')
coureur = dl.coureur_par_nom(nom)
if coureur is not None :
    print (coureur)
else :
    print('aucun coureur de ce nom')
    
print('liste des coureurs')
coureurs = dl.coureurs()
print(table_to_str(coureurs)) 
