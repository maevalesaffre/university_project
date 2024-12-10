package hotel;
public class Room {

   private int number;
   private Rank rank;
   private boolean busy;
   
   public Room(int number, Rank rank) {
      this.number = number;
      this.rank = rank;
      this.busy = false;
   }
   
   public Room(int number) {
      this(number, Rank.COMFORT);
   }
   
   public void upgrade() {
      this.rank = this.rank.nextUp();
   }
   
   public int getNumber() {
      return this.number;
   }
   
   public Rank getRank() {
      return this.rank;
   }
      
   public boolean isBusy() {
      return busy;
   }
   
   public void rent() {
      this.busy = true;
   }
   
   public void leave() {
      this.busy = false;
   }
}


