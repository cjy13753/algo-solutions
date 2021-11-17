import sys

n = int(sys.stdin.readline())
tmpCases = []
for _ in range(n):
    tmpCases.append(sys.stdin.readline().split()[0])
    
for ps in tmpCases:
    psStack = []
    flag = True
    for p in ps:
        if p == "(":
            psStack.append(p)
        else:
            if psStack:
                popped = psStack.pop()
                if popped == ")":
                    flag = False
                    break
            else:
                flag = False
                break
    
    print("YES") if flag == True and len(psStack) == 0 else print("NO")       
