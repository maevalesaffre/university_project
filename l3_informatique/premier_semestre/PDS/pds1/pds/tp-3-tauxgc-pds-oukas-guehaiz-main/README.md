# TP PDS - Taux de GC 

Étant donné un génome (c’est-à-dire un fichier contenant une liste de
bases qui peuvent être A, C, G ou T), il est intéressant de calculer
le taux d’apparition des bases G et C sur le nombre total de bases.

## Générateur de génome

Vous trouverez dans le depôt un générateur de génome aléatoire qui
vous permettra d’expérimenter sur des génomes de toutes les tailles
(plus petites que la mémoire de votre machine, vu le modèle très
simple de chargement du génome...).

Le programme [aleazard.c](aleazard.c) prend comme argument sur la ligne 
de command le nombre de bases à générer et affiche un génome aléatoire 
sur la sortie standard. Vous pouvez le sauvegarder avec une redirection : 
```sh
./aleazard 1000 > genome.txt
```

## Compter les GC

Le fichier [compteur-gc.c](compteur-gc.c) contient un programme
séquentiel qui compte le nombre de bases G ou C dans le génome. 
```
./compteur-gc genome.txt
``` 
et mésure le temps nécessaire à completer ce compte. Normalement, le
taux de G et C est presque de 50%.

L'objectif de ce TP est de paralleliser l'algorithme pour compter les
bases G et C.

## Question 1 

Modifiez le programme `compteur-gc.c` en `compteur-gc-par.c` 
- le nouveau programme prend en argument le nombre `t` de threads
  souhaités ;
- découpe le calcul du nombre de G et C en n threads, chacun traitant
  un n-ième du contenu du fichier ;
- affiche le taux une fois tous les calculs terminés. 

Pour tout valeurs de `t`, le nouveau programme parallèle doit afficher
le même taux que le programme sequentiel ! Testez sur certains valeurs
de `t`.

## Question 2 

Expérimentez la commande précédente, en faisant varier la taille du
génome à analyser et le nombre de threads pour trouver le nombre
optimal de threads suivant la taille du génome.


### Utilisation de gnuplot

Pour mener la campagne d’expériences, vous devez faire varier à la
fois la taille `n` des génomes et le nombre `t` de threads (par
exemple pour `n=10^2` à `10^9` et `t=2^0` à `2^5` cela donnera 48
expérimentations). En principe, pour qu’une mesure de temps soit
valable il faut, pour chaque expérience taille de génome/nombre de
threads, réaliser la moyenne sur plusieurs tests.

Vous pourrez avantageusement utiliser Gnuplot pour représenter votre
graphique en 3 dimensions. En admettant disposer d’un fichier res.dat
contenant sur chaque ligne la taille du génome, le nombre de threads
et le temps (séparés par des espaces), vous pourrez avec les commandes
suivantes obtenir une belle courbe.

```
gnuplot> set logscale x
gnuplot> set dgrid3d 30,30
gnuplot> set pm3d
gnuplot> splot ’res.dat’ using 1:2:3 with lines 
```
