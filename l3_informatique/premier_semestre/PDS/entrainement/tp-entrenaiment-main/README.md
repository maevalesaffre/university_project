# Consignes générales pour le rendu

## Comment rédiger vos reponses

Toutes vos réponses devront être rédigées dans `answers.c`. Vous
pouvez modifier `main.c` pour tester vos programmes mais attention,
aucune des modifications de `main.c` ne sera prise en compte pour
l'évaluation.

Pour chaque exercice, un exemple de `main` est écrit dans `main.c`.
Pour tester votre programme il faut donc :

1. Décommenter le main de l'exercice dans `main.c`
2. Compiler avec la commande `make`.
3. Exécuter le programme généré `prg`.

Pour obtenir une estimation de la note que vous aller obtenir vous
pouvez lancer `make test`.

## Comment rendre votre programme 

Pour rendre votre travail, devez déposer le fichier `answers.c` (et
_seulement ce fichier_ !) sur :

  https://prof.fil.univ-lille.fr/

Si vous vous trompez, vous pouvez déposer le fichier à nouveau jusqu'à
la fin de l'examen, le fichier retenu est toujours le dernier déposé.


# Exercice 1 - Liste de sous-répertoires

L’objectif de cet exercice est d’afficher la liste des
sous-répertoires (mais pas des sous-sous-répertoires) contenus dans un
répertoire. Prenons l’exemple de l’arborescence suivante :

    $ tree rep
    rep
    ├── a
    ├── b -> a
    ├── c
    │   └── d
    │       └── e
    ├── f -> c
    └── g
        └── h
    
    4 directories, 4 files
    $ ls -FR rep
    rep:
    a  b@  c/  f@  g/
    
    rep/c:
    d/
    
    rep/c/d:
    e
    
    rep/g:
    h

Tous les noms font une lettre.
L’option `-F` de `ls` permet d’indiquer par un caractère leur type :

-   `@` pour un lien symbolique,
-   `/` pour un répertoire,
-   rien pour un fichier normal.

L’option `-R` permet d’afficher récursivement le contenu des
répertoires imbriqués.

Nous voulons écrire une fonction `liste_sous_reps` telle que
`liste_sous_reps("rep")` affiche :

    rep/c
    rep/g
    rep/f

**Important:** `liste_sous_reps` devra utiliser la fonction `affiche_str` fournie pour afficher chaque ligne.

Notez que la fonction affiche aussi le lien symbolique `rep/f` parce
qu'il pointe vers un répertoire.


# Exercice 2 - Barrière avec activation

Un système consiste de `NTHREADS` threads, ayant le code suivant :

    void w(int tid, int step)
    {
        printf("W(%d) ETAPE %d\n", tid, step);
    }
    
    void *thread(void *arg)
    {
        int index = (int) arg;
    
        for (int i = 0; i<10; i++) {
            w(index, i);
            synch(index);
        }
        return NULL;
    }

Les threads font un calcul, representé ici par la fonction `w()`, en
10 étapes parallèles. Tous les threads doivent terminer l'étape `i`
avant d'entamer l'étape `i+1`.

Un thread de contrôle assure la synchronisation entre les threads :

    void *control(void *arg)
    {
        for (int i=0; i<10; i++) 
            activate();
    
        return NULL;
    }

La fonction `activate()` :

-   attend que tous les threads terminent l'étape courante ;
-   débloque tous les `NTHREADS` threads pour passer à l'étape
    suivante.

Pour résoudre l'exercice :

-   définir une structure de synchronisation entre les threads en
    utilisant un certain nombre de sémaphores.
-   coder la fonction `init(int nb_threads)` pour initialiser la
    structure de synchronisation, la fonction `activate(int
    nb_threads)` et la fonction `synch(int i)`.
