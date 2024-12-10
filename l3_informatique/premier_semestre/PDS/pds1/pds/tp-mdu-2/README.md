# Consignes générales pour le TP

# Compilation

Toutes vos réponses devront être rédigées dans le fichier `answers.c`
dans les fonctions correspondantes.

Un exemple de `main` est fourni dans `main.c`. Aucune modification de
`main.c` n'est prise en compte par les tests automatiques.  Utilisez `main.c`
pour tester manuellement votre programme.

Pour tester son programme il faut :
1. Compiler avec la commande `make`.
2. Exécuter le programme généré `prg`.

## Autoévaluation

Pour effectuer les tests automatiques et obtenir une estimation de
votre note, vous devez lancer `make test`. Le fait que les test soient
validés ne garantit pas la correction de votre code de manière absolue
; il y a toujours la possibilité d'un bug que les tests n'arrivent pas
à faire apparaître. Il s'agit d'un premier retour sur votre travail
qui peut vous être utile pour vérifier que vous avez atteint les
objectifs du TPs.

Si vous ne comprenez pas le résultat ou l'affichage d'un test, vous
pouvez toujours consulter son code dans `test_cases/testN.c`, avec `N`
le numéro du test.

# Parcours d'une hiérarchie

La commande UNIX **du** (*disk usage*) rapporte la taille disque utilisée
par un répertoire et l'ensemble de ses fichiers (y compris ses
sous-répertoires).

Deux tailles peuvent être prises en compte pour un fichier :
- la taille apparente, qui est le nombre d'octets contenus dans le
  fichier ;
- la taille réelle, qui correspond effectivement au nombre de blocs
  disque utilisés par le fichier.

Les champs `st_size` et `st_blocks` d'une structure de type `struct
stat` retournée par l'appel système `stat()` contiennent,
respectivement, la taille apparente et la taille réelle d'un fichier ;
vous trouverez plus de détails dans le manuel de `stat`.

Comme pour toutes les commandes réalisant un parcours d'une
hiérarchie, il faut préciser le traitement réalisé sur les liens
symboliques rencontrés : doivent-ils être suivis ou non ?

La commande `du` comporte donc deux options

- `-L` indiquant de suivre les liens symboliques ; ce qui n'est pas le
  cas par défaut ;
- `-b` indiquant de rapporter les tailles apparentes ; ce sont les
  tailles réelles qui sont rapportées sinon.

Dans la première partie de ce TP (exercices 1-3), on considère de ne pas suivre les 
liens symboliques et de calculer la taille réel (c'est-à-dire, les 
nombres de blocks). 

## Exercice 1 : Taille d'un seul fichier 

Proposer une implantation d'une fonction 
```c 
int du_single_file(const char *pathname);
```
qui retourne la taille occupée par le fichier désigné en paramètre.
Dans un première temps, comme on ne suit pas les liens symboliques, la
taille d'un lien symbolique est la taille occupée par le lien, et non
par le fichier visé.

En cas d'erreur (ficher non existant ou non accessible par exemple),
la fonction doit retourner `-1`.

## Exercice 2 : Est-ce que c'est un répertoire ?

Propose une implantation d'une fonction 
```c
int is_dir(const char *pathname);
```
qui :
- return `-1` si le fichier `pathname` n'existe pas ou s'il n'est pas accessible par le programme ;
- retourne `1` si `pathname` indique un répertoire ;
- retourne `0` dans tous les autres cas. 


## Exercice 3 : Taille d'un repertoire 

Proposez une implantation d'une fonction récursive :
```c
int du_file(const char *pathname);
```
Si le paramètre designe un fichier, elle appelle simplement la fonction 
`du_single_file(paramètre)` pour obtenir la taille du fichier ; si le 
paramètre designe un répertoire, elle s'appelle récursivement sur tous les fichiers 
du répertoire et fait la somme des tailles obtenues. 

En particulier, votre implantation devra faire attention à filtrer les
entrées des répertoires : il faut ignorer `.`  et `..` afin d'éviter
une boucle infinie.

## Exercice 4 : Suivre les liens symboliques

Une possible implantation consiste à définir une variable globale :
```c
int opt_follow_links = 0;
```
- quand cette variable vaut `0`, il ne faut pas suivre les liens symboliques 
  (c'est-à-dire, il faut retourner la taille du lien) ; 
- si elle vaut `1`, il faut suivre le liens symboliques (c'est-à-dire il faut 
  retourner la taille du fichier visé).
  
Vous pouvez changer la valeur de cette variable dans votre main en fonction 
des options passés sur la ligne de commande. Pour faire le parsing des options, 
vous pouvez utiliser la fonction `getopt()` de la librairie standard (utilisez 
la commande `man 3 getopt` pour obtenir plus d'informations). 

Modifiez l'implantation précédente de `du_single_file()` et de
`du_file()` pour suivre (ou pas) les liens symboliques en fonction de
la valeur de `opt_follow_links`.

## Exercice 5 : Taille réel ou apparente

On suit la même technique pour calculer la taille réel ou la taille
apparente. On defini une variable globale :

```c
int opt_apparent_size = 0;
```

on modifie le main pour prendre en compte l'option correspondante, et on modifie 
les fonctions `du_single_file()` et de `du_file()` pour calculer la taille 
réel (quand `opt_apparent_size==0`) ou la taille apparente 
(quand `opt_apparent_size==1)`. 

## Question : Comptage multiple ?

Un nœud qui serait référencé plusieurs fois dans une hiérarchie dont
on veut afficher la taille serait comptabilisé plusieurs fois. En quoi
est-ce gênant ? Comment s'en affranchir ?

Optionnel : essayez d'implementer une version `du_file` qui evite le problème du compage 
multiple. 

## Validation du TP 

Votre `du` sera validé par une série de tests. Vous devrez ainsi créer
des fichiers et des répertoires, de tailles différentes, avec ou sans
liens symboliques, etc. et vérifier que votre `du` donne les mêmes
résultats que la commande standard.

Pour vous comparer au `du` standard dans les salles du FIL, vous
utiliserez, suivant les cas de tests, les options :

- `-b` pour calculer la taille apparente,
- `-B 512` pour calculer l'occupation réelle,
- `-L` pour suivre les liens symboliques.

Ainsi, en notant `mdu` votre `du` :

- `./mdu rep` devra donner le même résultat final que `du -B 512 rep`,
- `./mdu -b rep` devra donner le même résultat final que `du -b rep`,
- l’option `-L` devra avoir le même sens pour les deux commandes.

Référez-vous au manuel pour en savoir plus sur `du`.


