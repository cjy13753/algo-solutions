import sys
sys.setrecursionlimit(10 ** 9)

def makePostOrder(preorder) -> list:
    length = len(preorder)
    if length <= 1:
        return preorder
    a=preorder[0]
    for i in range(1, length):
        if preorder[i] > a:
            return makePostOrder(preorder[1:i]) + makePostOrder(preorder[i:]) + [a]
        i += 1
    return makePostOrder(preorder[1:]) + [a]

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

postorder = makePostOrder(preorder)
for e in postorder:
    print(e)