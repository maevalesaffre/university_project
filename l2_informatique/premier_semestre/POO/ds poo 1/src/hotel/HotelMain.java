package hotel;

public class HotelMain {

   public static void main(String[] args) {

      Hotel hotel = new Hotel("California", 15);
                       
      int roomNumber = Integer.parseInt(args[0]);
      
      try {
         hotel.rentRoom(roomNumber);
         System.out.println("you rent room "+ roomNumber);
      } catch (RoomNotAvailableException e) {
         System.out.println("room "+ roomNumber+" is not free");
      }
   }

}
