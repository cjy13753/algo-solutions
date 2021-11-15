import sys

type = {')': '(', ']': '['}
price = {'(': 2, '[': 3}

ps = sys.stdin.readline().split()[0]

ptr = 0
stack = []
total = 0
success = True

while ptr <= len(ps) - 1:
    if ps[ptr] == '(' or ps[ptr] == '[':
        if len(stack) != 0:
            stack[-1][1] = False
        stack.append([ps[ptr], True])
    else:
        if len(stack) == 0:
            success = False
            break
        
        if type[ps[ptr]] != stack[-1][0]:
            success = False
            break
        else:
            p, flag = stack.pop()
            if flag == True:
                tmp = price[p]
                for i in range(len(stack)):
                    tmp *= price[stack[i][0]]
                total += tmp
    ptr += 1

if len(stack) != 0:
    success = False

print(total) if success == True else print(0)