# Exercice 1 : on ... do ....

Il s'agit d'implanter une commande `on` qui exécute une
seconde commande `cmd` si et seulement si l'exécution
d'une première commande `pred` se termine sur un succès :

```bash
on pred do cmd
```

On utilise cette commande comme sur l'exemple suivant :

```bash
on test -r spool/file do lpr spool/file
```

qui ne fait appel à la commande d'impression `lpr` que si le fichier
existe (commande `test`).

## SUGGESTIONS 

- Pour tester la commande `on`, utilisez les commandes `true` et `false` ;
  - `true` retourne toujours la valeur 0 ;
  - `false` retourne toujours la valeur 1.

  Souvenez-vous que par convention une valeur de retour égal à zéro
  signifie qu'il n'y a pas d'erreur.
  
  Par exemple 
  ```bash
  on true do cat file.txt
  ```
  montrera le contenu du fichier file.txt (s'il existe) sur la sortie standard. 

- Pour visualiser la valeur de retour d'un processus sur le terminal
  bash, utilisez la commande
  
		echo $?

- Pour savoir si votre programme est correct, vous pouvez lancer la commande 

		make test-docker 
		 
  qui lancera des tests sur votre programme. 



# Exercice 2 : do 

On désire implanter un programme `do` qui exécute indépendamment et
simultanément une série de commandes Shell données sur la ligne de
commande. L'exécution du programme se termine quand l'ensemble des
commandes a terminé. Le programme retourne alors un statut formé de la
conjonction (et, option `-a` (and)) ou de la disjonction (ou, option
`-o`) des statuts retournés par les commandes selon la valeur de
l'option.  Par défaut (si l'utilisateur n'a précisé ni `-a` ni `-o`),
on utilisera la conjonction.  La syntaxe est la suivante :

```bash
do [-a|-o] command...
```

On utilise cette commande `do` suivant l'exemple suivant :

```bash
do -a emacs firefox xterm
```

Implantez la commande `do`

## Coupe-circuit

Une utilisation possible de la commande `do` est de ne s'intéresser
qu'aux valeurs de retour des commandes lancées. Dans ce cas, il est
possible de conclure sur la valeur de retour de la commande `do` dès
qu'une des commandes retourne un succès (pour l'option `-o`, ou
retourne un échec pour l'option `-a`) : on parle de *conjonction ou
disjonction coupe-circuit*. Ce fonctionnement est activée par l'option
`-c` de la commande `do`.

Par exemple, la commande 
```bash
do -c false emacs 
```
sortira immédiatement avec valeur de retour 1 sans attendre la terminaison du processu `emacs`. 

De même, la commande
```bash
do -c -o true emacs 
```
sortira immédiatement avec valeur de retour 0, même si le processus
`emacs` reste en exécution. 

Implantez cette variation. 


## Commandes avec paramètres

Pour raffiner `do`, on désire que les commandes puissent
accepter des paramètres et ainsi utiliser la commande de la
manière suivante :

```bash
do -a "vim test.c" "xclock -update 1"
```

Pour implanter cette version de la commande `do`, vous pouvez utiliser
la librairie `makeargv.h/.c` fourni dans le dépôt qui sert à séparer
les arguments. Un exemple d'utilisation est dans le fichier
`args.c`. Nous vous conseillons d'expérimenter avec ce dernier avant
d'implanter la dernière version du deuxième exercice.

