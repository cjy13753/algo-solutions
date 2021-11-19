import sys
sys.setrecursionlimit(10 ** 9)

class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None

def build(root: Node) -> None:
    try:    
        while True:
            newNode = Node(int(input()))
            prevNode = root
            curNode = root
            direction = 'L'
            
            while curNode is not None:
                prevNode = curNode
                if newNode.key < curNode.key:
                    curNode = curNode.left
                    direction = 'L'
                else:
                    curNode = curNode.right
                    direction = 'R'
            if direction == 'L':
                prevNode.left = newNode
            else:
                prevNode.right = newNode
    except:
        return


def postorder(root: Node) -> None:
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.key)

root = Node(int(input()))
build(root)
postorder(root)