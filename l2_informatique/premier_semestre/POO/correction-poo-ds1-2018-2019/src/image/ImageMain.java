package image;

import java.io.File;


public class ImageMain {

	public static void main(String[] args) {

		File imageFile1 = new File("path1");
		File imageFile2 = new File("path2");
		
		Image img1 = Image.initImageFromFile(imageFile1);
		Image img2 = Image.initImageFromFile(imageFile2);
		
		int pixelDiff = 0;
		try {
			pixelDiff = img1.numberOfTooDifferentPixels(img2);
		} catch (BadImageFormatException e) {
			pixelDiff = img1.getWidth() * img1.getHeight();
		}
		
		System.out.println("number of different pixels is "+pixelDiff);
	}

}
