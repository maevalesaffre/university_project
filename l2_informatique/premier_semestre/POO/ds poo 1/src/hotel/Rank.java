package hotel;

public enum Rank {
   COMFORT, COSY, PREMIUM;

   public Rank nextUp() {
      if (this == PREMIUM) 
         return PREMIUM;
      else 
         return Rank.values()[this.ordinal() + 1];
   }
   
}