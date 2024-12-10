package hotel;

import static org.junit.Assert.*;

import org.junit.Test;

public class RoomTest {

   @Test
   public void upgradeLeadsToUpperRank() {
      Room room = new Room(1);
      assertEquals(Rank.COMFORT, room.getRank());
      room.upgrade();
      assertEquals(Rank.COSY, room.getRank());
      room.upgrade();
      assertEquals(Rank.PREMIUM, room.getRank());
      room.upgrade();
      assertEquals(Rank.PREMIUM, room.getRank());
   }
   

}
