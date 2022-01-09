'''
Summary - Attempt #1

Fail due to wrong answer
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
        pass

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recur(sliced_preorder, sliced_inorder):
            if len(sliced_preorder) < 1:
                return
            
            root_val = sliced_preorder[0]
            root = TreeNode(root_val)

            if len(sliced_preorder) == 1:
                return root

            root_idx_for_inorder = inorder.index(root_val)
            left_subtree_size = len(inorder[:root_idx_for_inorder])
            
            root.left = recur(sliced_preorder[1:left_subtree_size + 1], sliced_inorder[:root_idx_for_inorder])
            root.right = recur(sliced_preorder[left_subtree_size + 1:], sliced_inorder[root_idx_for_inorder + 1:])

            return root


        return recur(preorder, inorder)




Solution()