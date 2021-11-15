import sys

ps = sys.stdin.readline().split()[0]

matching = {'(': ')', '[': ']'}

parenStack = []
scoreStack = [0]
flag = True
for c in ps:
    if c == '(' or c == '[':
        parenStack.append(c)
        scoreStack.append(0)
    else:
        if len(parenStack) == 0:
            flag = False
            break
            
        popped = parenStack.pop()
        if matching[popped] != c:
            flag = False
            break
        else:
            last = scoreStack.pop()
            if popped == '(':
                scoreStack[-1] += 2 * last or 2
            else:
                scoreStack[-1] += 3 * last or 3

if len(parenStack) != 0:
    flag = False

print(scoreStack.pop()) if flag == True else print(0)