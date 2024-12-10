package expression.operator;

public class Multiplication implements Operator {

   public int compute(int x, int y) {
      return x * y;
   }

   public char getChar() {
      return 'x';
   }

   
}
