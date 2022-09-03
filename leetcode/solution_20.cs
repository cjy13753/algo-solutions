// Time Complexity: O(N)
// Runtime: 128 ms, faster than 27.17% of C# online submissions for Valid Parentheses.

// Space Complexity: O(N)
// Memory Usage: 36.8 MB, less than 41.60% of C# online submissions for Valid Parentheses.


public class Solution {
    public bool IsValid(string s) {
		var parentheses = s.ToArray();
		var openBrackets = new HashSet<char> { '(', '{', '[' };
		var bracketMap = new Dictionary<char, char>{
			{')', '('},
			{'}', '{'},
			{']', '['},
		};
		
		var stack = new Stack<char>();
		
		foreach (var paren in parentheses)
		{
			if (openBrackets.Contains(paren))
			{
				stack.Push(paren);
			}
			else
			{
				if (stack.Count == 0)
				{
					return false;
				}
				
				if (bracketMap[paren] == stack.Peek())
				{
					stack.Pop();
				}
				else
				{
					return false;
				}
			}
		}
		
		return stack.Count > 0 ? false : true;
	}
}