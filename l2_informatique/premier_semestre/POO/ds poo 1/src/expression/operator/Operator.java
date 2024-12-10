package expression.operator;

public interface Operator {

   /** performs the operation of this operator with given two operands
    * @param x the left operand
    * @param y the right operand
    * @return the result of the operation
    */
   int compute(int x, int y);
   
   /** get the char used to display this operator
    * @return the char used to display this operator
    */
   char getChar();
}
