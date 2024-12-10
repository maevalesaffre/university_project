package zoo;

import java.util.ArrayList;
import java.util.List;

public class Zoo {

	
	private List<Animal> animals;
	
	public Zoo() {
		this.animals = new ArrayList<>();
	}
	
	public void addAnimal(Animal mam) {
		this.animals.add(mam);
	}
	
	public int getNbTotalLegs() {
		int result = 0;
		for(Animal m : this.animals) {
			result += m.getNbLegs();
		}
		return result;
	}
}
