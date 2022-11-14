// Time Complexity: Insert-O(n), Search-O(n), StartsWith-O(n), where n is the number of characters in the given string
// Space Complexity: ?

/*

The internal data structure would look like this.
A node object would have the following two fields.
1. bool couldBeTheEnd
2. Node[] followingCharacters.

when inserting a new word, the process would look like this.
starting with the root node, try to find out if each character is in the followingCharacters.
(but if followingCharacters is null, instantiate one)
if there is no character node in the chain, make a new one and do the loop.

*/

public class Trie {
    private CharacterNode root;

    public Trie() {
        root = new CharacterNode('?');
    }
    
    public void Insert(string word) {
        CharacterNode pointer = root;
        foreach (var c in word)
        {
            if (pointer.followingCharacters.ContainsKey(c))
            {
                pointer = pointer.followingCharacters[c];
            }
            else
            {
                var newNode = new CharacterNode(c);
                pointer.followingCharacters[c] = newNode;
                pointer = newNode;
            }
        }
        pointer.couldBeTheEnd = true;
    }
    
    public bool Search(string word) {
        var pointer = root;
        
        foreach (var c in word)
        {
            if (pointer.followingCharacters.ContainsKey(c))
            {
                pointer = pointer.followingCharacters[c];
            }
            else
            {
                return false;
            }
        }
        
        return pointer.couldBeTheEnd;
    }
    
    public bool StartsWith(string prefix) {
        var pointer = root;
        
        foreach (var c in prefix)
        {
            if (pointer.followingCharacters.ContainsKey(c))
            {
                pointer = pointer.followingCharacters[c];
            }
            else
            {
                return false;
            }
        }
        
        return true;
    }
}

public class CharacterNode
{
    public char character;
    public bool couldBeTheEnd = false;
    public Dictionary<char, CharacterNode> followingCharacters = new();
    
    public CharacterNode(char c)
    {
        character = c;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */