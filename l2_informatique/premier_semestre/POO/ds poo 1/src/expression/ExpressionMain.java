package expression;

import expression.operator.Addition;
import expression.operator.Multiplication;

public class ExpressionMain {

   public static void main(String[] args) {
      BinaryExpression expAdd = new BinaryExpression(1, new Addition(), 2);
      BinaryExpression expMul = new BinaryExpression(6, new Multiplication(), 7);

      System.out.println(expAdd+ " = " + expAdd.getValue());
      System.out.println(expMul+ " = " + expMul.getValue());
   }

}
