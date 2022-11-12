// Time Complexity: O(n) where n is the number of elements in the given array because each number is pushed into and popped from the stack in the total of 4 times.
// Space Complexity: O(n) because there can be at most (n/2) number of numbers and in the worst case, they can all be pushed into the stack


public class Solution {
    public int EvalRPN(string[] tokens) {
        if (tokens.Length == 1)
        {
            return Int32.Parse(tokens[0]);
        }
        
        var stack = new Stack<int>();
        var operators = new HashSet<string> { "+", "-", "*", "/" };
        
        foreach (var token in tokens)
        {
            if (operators.Contains(token))
            {
                var operand2 = stack.Pop();
                var operand1 = stack.Pop();
                var result = ApplyOperator(token, operand1, operand2);
                stack.Push(result);
            }
            else
            {
                stack.Push(Int32.Parse(token));
            }
        }
        
        
        return stack.Pop();
    }
    
    private int ApplyOperator(string _operator, int operand1, int operand2)
    {
        var result = 0;
        switch (_operator)
        {
            case "+":
                result = operand1 + operand2;
                break;
            case "-":
                result = operand1 - operand2;
                break;
            case "*":
                result = operand1 * operand2;
                break;
            case "/":
                result = operand1 / operand2;
                break;
        }
        return result;
    }
}