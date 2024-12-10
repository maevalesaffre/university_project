package premium.util;

/**
 * define a category with tree level silver, gold and platinum,
 * value of a category depends of some point levels
 */
public enum Category {
	SILVER, GOLD, PLATINUM;
	
	/** points level to reach GOLD category */
	public static final int GOLD_POINTS = 1000;
	/** points level to reach PLATINUM category */
	public static final int PLATINUM_POINTS = 2500;
	
	/** returns the category according to given number of points
	 * @param points a number of points, we want the corresponding category
	 * @return the category according to <code>points</code>
	 */
	public static Category fromPoints(int points) {
		if (points > Category.PLATINUM_POINTS) {
			return Category.PLATINUM; 
		} 
		else if (points > Category.GOLD_POINTS) {
			return Category.GOLD; 
		}  
		else
			return Category.SILVER;
	}
}
