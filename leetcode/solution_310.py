'''
Summary - Attempt #1

Your own answer?: No
Reference: https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
Runtime: 504 ms, faster than 23.94% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 25.4 MB, less than 13.37% of Python3 online submissions for Minimum Height Trees.

Basic Idea: Topological Sort
'''


import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        n = 6
        edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        print(self.findMinHeightTrees(n, edges))

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj_list = [set() for _ in range(n)] # [node1: [incoming neighbors], node2: [incoming neighbors]]

        for e in edges:
            src, dst = e
            adj_list[src].add(dst)
            adj_list[dst].add(src)

        leaves = []
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)
        
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                popped = adj_list[leaf].pop()
                adj_list[popped].remove(leaf)
                if len(adj_list[popped]) == 1:
                    newLeaves.append(popped)
            leaves = newLeaves

        return leaves

Solution()