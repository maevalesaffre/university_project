package hotel;

public class Hotel {
   
   private String name;
   private Room[] rooms;
   
   public Hotel(String name, int nbRooms) {
      this.name = name;
      this.rooms = new Room[nbRooms];
      for (int i = 0 ; i < nbRooms; i ++) {
         this.rooms[i] = new Room(i+1);
      }
   }
      
   /** get the room with given number if it exists
    * @param number the wanted room number
    * @return the room
    * @throws RoomNotAvailableException if no room has given number
    */
   public Room getRoom(int number) throws RoomNotAvailableException {
      try {
         return this.rooms[number-1];
      }
      catch(ArrayIndexOutOfBoundsException e) {
         throw new RoomNotAvailableException("room "+(number-1)+" does not exist");
      }
   }
   
   public int getNbRooms() {
      return this.rooms.length;
   }
   
   public int nbAvailableRooms() {
      int result = 0;
      for (Room r : this.rooms) {
         if ( ! r.isBusy() ) {
            result = result + 1;
         }
      }
      return result;
   }
   
   public void upgradeRoom(int number) {
      this.getRoom(number).upgrade();
   }
   
   /** rent the room with given number if not busy
    * @param number the number of the room
    * @throws RoomNotAvailableException if the room is not free 
    */
   public void rentRoom(int number) throws RoomNotAvailableException {
      if (this.getRoom(number).isBusy())
         throw new RoomNotAvailableException("room "+number+" is busy");
      this.getRoom(number).rent();
   }
   
   public void checkOut(int number) {
      this.getRoom(number).leave();
   }
   
   public String getName() {
      return this.name;
   }
   
   public boolean equals(Object o) {
      if (! (o instanceof Hotel) )
         return false;
      Hotel other = (Hotel) o;
      return this.name.equals(other.name) && this.getNbRooms() == other.getNbRooms();
   }
   
}
