'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 45m

Time Complexity: O(N) for all opeartions
Runtime: 170 ms, faster than 78.69% of Python3 online submissions for Implement Trie (Prefix Tree).

Space Complexity: O(N) for insert and O(1) for search and startsWith
Memory Usage: 27.8 MB, less than 91.49% of Python3 online submissions for Implement Trie (Prefix Tree).
'''


class Trie:
    def __init__(self):
        self.ds = {}

    def insert(self, word: str) -> None:
        cur_ds = self.ds
        for c in word:
            if not c in cur_ds:
                cur_ds[c] = {}
            cur_ds = cur_ds[c]
        cur_ds[None] = None

    def search(self, word: str) -> bool:
        ret = True
        cur_ds = self.ds
        for c in word:
            if not c in cur_ds:
                return False
            cur_ds = cur_ds[c]          

        if None not in cur_ds:
            return False
        
        return ret
        
    def startsWith(self, prefix: str) -> bool:
        ret = True
        cur_ds = self.ds
        for c in prefix:
            if not c in cur_ds:
                return False
            cur_ds = cur_ds[c]          
        
        return ret

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.ds)
param_2 = obj.search("apple")
print(param_2)
param_3 = obj.startsWith("app")
print(param_3)