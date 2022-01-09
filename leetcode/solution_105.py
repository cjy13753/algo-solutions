'''
Summary - Attempt #2

Your own answer?: No
Reference: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/981152/Recursion-or-Explanation-%2B-Visuals-or-Python
Runtime: 291 ms, faster than 16.49% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.5 MB, less than 10.83% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

Memo: It's almost the same answer as my previous attempt. Only omitted 'recur' wrapper function, and it just worked. Don't know why.
'''


import sys
from typing import List, Optional
input = sys.stdin.readline

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        self.buildTree(preorder, inorder)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) < 1:
            return
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        if len(preorder) == 1:
            return root

        root_idx_for_inorder = inorder.index(root_val)
        left_subtree_size = len(inorder[:root_idx_for_inorder])
        
        root.left = self.buildTree(preorder[1:left_subtree_size + 1], inorder[:root_idx_for_inorder])
        root.right = self.buildTree(preorder[left_subtree_size + 1:], inorder[root_idx_for_inorder + 1:])

        return root

Solution()