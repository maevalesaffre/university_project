package expression;

import expression.operator.Operator;

public class BinaryExpression {

   private int leftOperand;
   private int rightOperand;
   private Operator operator;
   
   public BinaryExpression(int left, Operator op, int right) {
      this.leftOperand = left;
      this.rightOperand = right;
      this.operator = op;
   }

   public int getValue() {
      return this.operator.compute(this.leftOperand, this.rightOperand);
   }
   
   public String toString() {
      return ""+ this.leftOperand + this.operator.getChar() + this.rightOperand;
   }
   
}
