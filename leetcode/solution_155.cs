// Time Complexity: Push-O(1), Pop-O(1), Top-O(1), GetMin-O(1)
// Space Complexity: O(n) 

public class MinStack {
    Stack<int> primaryStack = new();
    Stack<int> minStack = new();

    public MinStack() {
    }
    
    public void Push(int val) {
        primaryStack.Push(val);
        if (minStack.Count == 0)
        {
            minStack.Push(val);
        }
        else
        {
            var prevMin = minStack.Peek();
            minStack.Push(Math.Min(prevMin, val));
        }
    }
    
    public void Pop() {
        primaryStack.Pop();
        minStack.Pop();
    }
    
    public int Top() {
        return primaryStack.Peek();
    }
    
    public int GetMin() {
        return minStack.Peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */