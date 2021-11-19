def printAsChar(num: int) -> None:
    print(chr(num + ord('A')), end='')


def preorder(tree, root):
    if root == -1:
        return

    printAsChar(root)
    preorder(tree, tree[root][0])
    preorder(tree, tree[root][1])

def inorder(tree, root):
    if root == -1:
        return
    
    inorder(tree, tree[root][0])
    printAsChar(root)
    inorder(tree, tree[root][1])

def postorder(tree, root):
    if root == -1:
        return
    
    postorder(tree, tree[root][0])
    postorder(tree, tree[root][1])
    printAsChar(root)

# 트리 만들기
tree = [[-1, -1] for _ in range(26)]
for _ in range(int(input())):
    node, left, right = [ord(val) - ord('A') if val != '.' else -1 for val in input().split()]
    tree[node][0] = left
    tree[node][1] = right

root = 0
preorder(tree, root)
print()
inorder(tree, root)
print()
postorder(tree, root)