import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numCases = int(input())
        for _ in range(numCases):
            numNodes = int(input())
            preorder = list(map(int, input().split()))
            inorder = list(map(int, input().split()))
            res = self.findPostorder(preorder, inorder)
            for i in res:
                print(i, end=' ')
            print()
    
    def findPostorder(self, preorder: list, inorder: list) -> list:
        if len(preorder) <= 1:
            return preorder

        rootIdxPreorder = 0
        root = preorder[rootIdxPreorder]
        rootIdxInorder = 0
        while inorder[rootIdxInorder] != root:
            rootIdxInorder += 1
        
        leftPortionLength = len(inorder[:rootIdxInorder])

        rightIdxInPreorder = 1 + leftPortionLength

        preLeft = preorder[1:rightIdxInPreorder]
        inLeft = inorder[:rootIdxInorder]
        leftRes = self.findPostorder(preLeft, inLeft)

        preRight = preorder[rightIdxInPreorder:]
        inRight = inorder[rootIdxInorder + 1:]
        rightRes = self.findPostorder(preRight, inRight)

        return leftRes + rightRes + [root]

Solution()