package image;

public class Pixel {

	public static final int WHITE_LEVEL = 255;
	
	private int grayLevel;
	
	public Pixel(int grayLevel) {
		this.grayLevel = grayLevel;
	}
	
	public int getGrayLevel() {
		return this.grayLevel;
	}

	public int grayLevelDifference(Pixel other) {
		return Math.abs(this.grayLevel - other.grayLevel);
	}
}
