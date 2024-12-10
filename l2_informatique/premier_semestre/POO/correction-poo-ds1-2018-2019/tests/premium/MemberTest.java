package premium;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertSame;

import org.junit.Test;

import premium.util.Category;

public class MemberTest {

	@Test
	public void testAddPointsChangePoints() {
		Member member = new Member("Timoleon");
		assertEquals(0, member.getNbPoints());
		member.addPoints(10);
		assertEquals(10, member.getNbPoints());
		member.addPoints(1000);
		assertEquals(10010, member.getNbPoints());		
	}

	@Test
	public void testAddPointsChangeCategory() {
		Member member = new Member("Timoleon");
		assertSame(Category.SILVER,member.getCategory() );
		assertEquals(0, member.getNbPoints());
		//add point and SILVER
		member.addPoints(10);
		assertEquals(10, member.getNbPoints());
		assertSame(Category.SILVER,member.getCategory() );
		// add points and GOLD
		member.addPoints(Category.GOLD_POINTS);
		assertEquals(10+Category.GOLD_POINTS, member.getNbPoints());
		assertSame(Category.GOLD,member.getCategory() );
		// add points and PLATINUM
		member.addPoints(Category.PLATINUM_POINTS);
		assertEquals(10+Category.PLATINUM_POINTS+Category.GOLD_POINTS, member.getNbPoints());
		assertSame(Category.PLATINUM,member.getCategory() );		
	}
}
