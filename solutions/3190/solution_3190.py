import sys
from collections import deque

boardSize = int(sys.stdin.readline())
numApples = int(sys.stdin.readline())
apples = [list(map(int, sys.stdin.readline().split())) for _ in range(numApples)]
shifting = deque(sys.stdin.readline().split() for _ in range(int(sys.stdin.readline())))

direction = {'S': (1, 0), 'W': (0, -1), 'N': (-1, 0), 'E': (0, 1)}
toWhereOnShifting = {'D': {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}, \
                     'L': {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}}

curDirection = 'E'
rowMove = direction['E'][0]
colMove = direction['E'][1]

snake = deque([[1,1]])
time = 0

flag = True
while True:
    time += 1

    snake.appendleft([snake[0][0] + rowMove, snake[0][1] + colMove])
    
    # snake가 자기 자신을 만나면 게임 종료
    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            flag = False
    if flag == False:
        break

    # snake가 벽에 닿으면 게임 종료
    if snake[0][0] < 1 or snake[0][0] > boardSize or snake[0][1] < 1 or snake[0][1] > boardSize:
        break

    # 사과를 안 먹으면 꼬리가 잘림, 사과 먹으면 사과 없애주기
    if snake[0] not in apples:
        snake.pop()
    else:
        apples.remove(snake[0])
    

    # 적절한 시간이 되면 방향이 바뀜
    if shifting and int(shifting[0][0]) == time:
        _, leftOrRight = shifting.popleft()
        directionPairs = toWhereOnShifting[leftOrRight]
        curDirection = directionPairs[curDirection]
        rowMove, colMove = direction[curDirection]

print(time)

