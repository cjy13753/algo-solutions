import sys
sys.setrecursionlimit(10 ** 9)

def convertToPostOrder(preorder: list, start: int, end: int) -> None:
    if start > end:
        return
    
    root = preorder[start]

    idx = start + 1
    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1
    
    convertToPostOrder(preorder, start + 1, idx - 1)
    convertToPostOrder(preorder, idx, end)
    
    print(root)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

convertToPostOrder(preorder, 0, len(preorder) - 1)
