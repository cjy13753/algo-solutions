''' 
Summary - Attempt #1

Your own answer?: Yes
Time spent: 1h30m

Runtime: 248 ms, faster than 25.03% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 18.9 MB, less than 64.91% of Python3 online submissions for Serialize and Deserialize Binary Tree.
'''

import sys
from collections import deque
input = sys.stdin.readline

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        
        ans = []
        queue = deque()
        queue.append(root)
        NIL_VAL = "N"
        NIL = TreeNode(NIL_VAL)

        while queue:
            node: TreeNode = queue.popleft()

            ans.append(str(node.val))
            
            if node.val == "N":
                continue

            
            if node.left == None:
                queue.append(NIL)
            else:
                queue.append(node.left)
            
            if node.right == None:
                queue.append(NIL)
            else:
                queue.append(node.right)

        return ' '.join(ans)


    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        parsed = deque(data.split(' '))
        queue = deque()
        root = TreeNode(parsed.popleft())
        queue.append(root)

        while queue:
            node: TreeNode = queue.popleft()
            l = parsed.popleft()
            if l != "N":
                lNode = TreeNode(int(l))
                node.left = lNode
                queue.append(lNode)

            r = parsed.popleft()
            if r != "N":
                rNode = TreeNode(int(r))
                node.right = rNode
                queue.append(rNode)

        return root

# Your Codec object will be instantiated and called as such:
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ser.serialize(ans))