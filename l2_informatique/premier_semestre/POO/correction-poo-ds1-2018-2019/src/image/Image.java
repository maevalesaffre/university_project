package image;

import java.io.File;

/**
 * An image made of an two dimensionnal arrays of pixels
 *
 */
public class Image {

	private static final int DIFFERENCE_THRESHOLD = 5;
	
	private Pixel[][] pixels;
	
	/** creatre an image withgiven height and width
	 * @param width with of this image
	 * @param height height of this image
	 */
	public Image(int width, int height) {
		this.pixels = new Pixel[width][height];
		for (int x = 0 ; x < this.getWidth() ; x++) {
			for (int y = 0; y < this.getHeight(); y++) {
				this.pixels[x][y] = new Pixel(Pixel.WHITE_LEVEL);
			}
		}
	}
	

	/** return the width for this image
	 * @return the width for this image
	 */
	public int getWidth() {
		return this.pixels.length;
	}
	/** return the height for this image
	 * @return the height for this image
	 */
	public int getHeight() {
		return this.pixels[0].length;
	}
	
	/** returns the pixel at given coordinate
	 * @param x x coordinate
	 * @param y y coordinate
	 * @return the pixel at given coordinate
	 */
	public Pixel getPixel(int x, int y) {
		return this.pixels[x][y];
	}
	
	
	/** return the image create from file
	 * @param f a file with data for this image
	 * @return the image create from file
	 */
	public static Image initImageFromFile(File f) {
		// initialize this.pixels from data in file f
		return new Image(1,1);
	}
	
	/** return the number of pixels that are too different between this image and the other given image.
	 * Too different means that their gray levels differ from more than DIFFERENT_THRESHOLD
	 * @param other the other image to compare this with
	 * @return the number of too different pixels
	 * @throws BadImageFormatException if both images are of different height or width
	 */
	public int numberOfTooDifferentPixels(Image other) throws BadImageFormatException {
		if (this.getWidth() != other.getWidth() || this.getHeight() != other.getHeight() ) 
			throw new BadImageFormatException();
		int differentPixels = 0;
		for (int x = 0 ; x < this.getWidth() ; x++) {
			for (int y = 0; y < this.getHeight(); y++) {
				int grayDifference = this.getPixel(x, y).grayLevelDifference(other.getPixel(x, y));
				if (grayDifference > Image.DIFFERENCE_THRESHOLD) {
					differentPixels = differentPixels +1;
				}
			}
		}
		return differentPixels;
	}
	
	
}
