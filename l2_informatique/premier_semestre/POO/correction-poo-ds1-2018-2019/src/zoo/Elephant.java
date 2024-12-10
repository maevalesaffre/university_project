package zoo;

public class Elephant implements Animal {

	private int weight;
	
	public Elephant(int weight) {
		this.weight = weight;
	}
	
	@Override
	public int getNbLegs() {
		return 4;
	}

	@Override
	public boolean isCarnivorous() {
		return false;
	}

}
