package zoo;

import java.util.ArrayList;
import java.util.List;

public class ZooMain {

	
    public static void main(String[] args) {
	Zoo aZoo = new Zoo();
	aZoo.addAnimal(new Elephant(1500));
	aZoo.addAnimal(new Anaconda());
    }
    
}

/*

Q1.2
Il n'est pas nécessaire de compléter la classe Zoo car les classes
Elephant et Anaconda implémentant l'interface Animal, les instances de
ces classes sont aussi du type Animal. Ils peuvent donc être utilisés
comme paramètre de la méthode addAnimal de Zoo.

Q2.
Les valeurs possibles pour le type T sont : 
Elephant, Animal et Object

 */
