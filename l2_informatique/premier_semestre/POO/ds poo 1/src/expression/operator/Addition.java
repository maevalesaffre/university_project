package expression.operator;

public class Addition implements Operator {

   public int compute(int x, int y) {
      return x + y ;
   }

   public char getChar() {
      return '+';
   }

}
