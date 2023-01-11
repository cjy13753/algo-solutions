public class LRUCache {
    private Dictionary<int, Node> dict = new();
    private LinkedList linkedList = new();
    private int capacity;
    private int usage = 0;

    private class LinkedList
    {
        public Node head = new Node(-1, -1); // dummy node
        public Node tail = new Node(-1, -1); // dummy node

        public LinkedList()
        {
            head.next = tail;
            tail.prev = head;
        }
    }

    private class Node
    {
        public int key;
        public int val;
        public Node prev = null;
        public Node next = null;

        public Node(int key, int val)
        {
            this.key = key;
            this.val = val;
        }
    }


    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int Get(int key) {
        if (dict.TryGetValue(key, out var node))
        {
            UpgradeToMRU(node);
            // printAllNodes();
            return node.val;
        }
        else
        {
            return -1;
        }
    }
    
    public void Put(int key, int value) {
        if (dict.TryGetValue(key, out var node))
        {
            node.val = value;
            UpgradeToMRU(node);
            // printAllNodes();
            return;
        }

        if (usage < capacity)
        {
            usage++;
        }
        else
        {
            evictLRU();
        }

        var newNode = new Node(key, value);
        dict[key] = newNode;
        InsertAtFront(newNode);
        // printAllNodes();
    }

    // Put the given node at the very front of the doubly linked list
    private void UpgradeToMRU(Node node)
    {
        var prev = node.prev;
        var next = node.next;
        prev.next = next;
        next.prev = prev;

        var prevHead = linkedList.head.next;
        linkedList.head.next = node;
        node.prev = linkedList.head;
        node.next = prevHead;
        prevHead.prev = node;
        // Console.WriteLine($"key: {node.key}, value: {node.val} is upgraded to MRU");
    }

    private void InsertAtFront(Node node)
    {
        var prevHead = linkedList.head.next;
        linkedList.head.next = node;
        node.prev = linkedList.head;
        
        node.next = prevHead;
        prevHead.prev = node;
        // Console.WriteLine($"key: {node.key}, value: {node.val} is being inserted at front");
    }

    private void evictLRU()
    {
        var nodeToEvict = linkedList.tail.prev;
        var keyToEvict = nodeToEvict.key;
        // Console.WriteLine($"{keyToEvict} is evicted");
        dict.Remove(keyToEvict);
        
        nodeToEvict.prev.next = linkedList.tail;
        linkedList.tail.prev = nodeToEvict.prev;
    }

    private void printAllNodes()
    {
        var result = "";
        var node = linkedList.head;
        while (node is not null)
        {
            var key = node.key;
            var value = node.val;
            var pair = $"({key}, {value}), ";
            result += pair;
            node = node.next;
        }

        Console.WriteLine(result);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */