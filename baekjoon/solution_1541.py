import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        expression = input().strip()
        self.minimumResult(expression)

    def minimumResult(self, expression: str) -> None:
        ans = 0
        switch = False
        
        i = 0
        tmp = ''
        
        # 1. 다음 연산자가 나올 때까지의 모든 글자를 임시로 합쳐놓는다.
        # 2. 연산자가 나오면 그때까지 합친 글자를 int로 변환하고 switch의 상태에 따라 더하거나 뺴고 tmp를 ''로 초기화시켜준다.
            # 2-1. switch가 False면 값을 ans에 더해준다
            # 2-2. switch가 True면 값을 ans에서 빼준다.
        # 3. - 연산자가 나올 경우 switch의 상태를 True로 바꿔준다.
        while i < len(expression):
            digit = expression[i]
            if digit != '-' and digit != '+':
                tmp += expression[i]
            else:
                if switch == False:
                    ans += int(tmp)
                    if digit == '-':
                        switch = True
                else:
                    ans -= int(tmp)
                tmp = ''
            i += 1
        
        if switch == False:
            ans += int(tmp)
        else:
            ans -= int(tmp)

        print(ans)

Solution()