'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 25m
Runtime: 48 ms, faster than 14.75% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 14.4 MB, less than 33.43% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
'''

import sys
input = sys.stdin.readline

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        pass

    def bstToGst(self, root: TreeNode) -> TreeNode:
        accum = [0]

        def dfs(root: TreeNode) -> None:
            if root == None:
                return
            
            dfs(root.right)
            root.val += accum[0]
            accum[0] = root.val
            dfs(root.left)
        
        dfs(root)
        return root

Solution()