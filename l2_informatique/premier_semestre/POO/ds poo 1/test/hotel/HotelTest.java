package hotel;

import static org.junit.Assert.*;
import org.junit.*;


public class HotelTest {

   private static final int NB_ROOMS = 10;
   private static final int EXISTING_ROOM_NUMBER = 5;
   
   private Hotel someHotel;
   
   @Before
   public void initTest() {
      this.someHotel = new Hotel("forTest",NB_ROOMS);
   }

   @Test
   public void roomIsBusyAfterRentRoom() throws RoomNotAvailableException {
      assertFalse(this.someHotel.getRoom(EXISTING_ROOM_NUMBER).isBusy());
      this.someHotel.rentRoom(EXISTING_ROOM_NUMBER);
      assertTrue(this.someHotel.getRoom(EXISTING_ROOM_NUMBER).isBusy());
   }
   
   @Test(expected=RoomNotAvailableException.class)
   public void rentRoomThrowsExceptionIfRoomBusy() throws RoomNotAvailableException {
      try {
         assertFalse(this.someHotel.getRoom(EXISTING_ROOM_NUMBER).isBusy());
         this.someHotel.rentRoom(EXISTING_ROOM_NUMBER);
         assertTrue(this.someHotel.getRoom(EXISTING_ROOM_NUMBER).isBusy());
      }
      catch(RoomNotAvailableException e) {
         fail(); // test fail if first rentRoom throws exception
      }
      // following throws exception
      this.someHotel.rentRoom(EXISTING_ROOM_NUMBER);      
   }
   
   @Test(expected=RoomNotAvailableException.class)
   public void rentRoomThrowsExceptionIfNumberDoesNotExist() throws RoomNotAvailableException {
      this.someHotel.rentRoom(NB_ROOMS + 10);
   }
}
