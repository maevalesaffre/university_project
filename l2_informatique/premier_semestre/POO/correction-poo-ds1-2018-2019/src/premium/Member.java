
package premium;

import premium.util.Category;

/** Define a Member with points and a specific Category 
 * 
 */
public class Member {

	private int nbPoints;
	private Category category;
	private final String name;
	
	/** create a member with given name and 0 point and silver category
	 * @param name the name of this memeber
	 */
	public Member(String name) {
		this.name = name;
		this.nbPoints = 0;
		this.setCategoryFromPoints();
	}
	
	/** return the name of this member
	 * @return the name of this member
	 */
	public String getName() {
		return this.name;
	}

	/** return the number of points of this member
	 * @return the number of points of this member
	 */
	public int getNbPoints() {
		return this.nbPoints;
	}

	/** add points to this member and update its category if needed
	 * @param newPoints the added points
	 */
	public void addPoints(int newPoints) {
		this.nbPoints = this.nbPoints + newPoints;
		this.setCategoryFromPoints();		
	}

	/**
	 * set the category depending on the number of points
	 */
	private void setCategoryFromPoints() {
		this.category = Category.fromPoints(this.nbPoints);		
	}

	/** return the category of this member
	 * @return the category of this member
	 */
	public Category getCategory() {
		return this.category;
	}

	/** two members are equals if they have same name and same number of points
	 * @see java.lang.Object#equals(java.lang.Object)
	 */
	public boolean equals(Object o) {
		if (o instanceof Member) {
			Member other = (Member) o;
			return this.name.equals(other.name) && this.nbPoints == other.nbPoints;
		}
		else
			return false;
	}
}
