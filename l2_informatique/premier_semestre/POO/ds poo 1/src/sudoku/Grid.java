package sudoku;

public class Grid {

   public static final int SQUARE_SIZE = 3;
   public static final int SIZE = SQUARE_SIZE * SQUARE_SIZE ;
   
   private int[][] grid;
   
   public Grid() {
      this.grid = new int[SIZE][SIZE];
      for (int i = 0; i < SIZE; i++) 
         for (int j = 0; j < SIZE; j++)
            this.grid[i][j] = 0;
   }

   
   public boolean setNumber(int number, int column, int row) {
      boolean result = this.notInRow(number, row) && 
                       this.notInColumn(number, column) && 
                       this.notInSquare(number, column, row);
      if (result) {
         this.grid[column][row] = number;
      }
      return result;
   }

   private boolean notInRow(int number, int row) {      
      for (int column = 0; column < SIZE ; column++) {
         if (this.grid[column][row] == number)
            return false;
      }
      return true;
   }
   

   private boolean notInColumn(int number, int column) {
      for (int row = 0; row < SIZE ; row++) {
         if (this.grid[column][row] == number)
            return false;
      }
      return true;
   }

   private boolean notInSquare(int number, int column, int row) {
      int baseColumn = column - column % SQUARE_SIZE + 1;
      int baseRow = row - row % SQUARE_SIZE + 1;
      for (int col = 0; col < SQUARE_SIZE; col++) {
         for (int ro = 0; ro < SQUARE_SIZE; ro++) {
            if (this.grid[baseColumn+col][baseRow+ro] == number)
               return false;
         }
      }
      return true;
   }
   
   
   
}
