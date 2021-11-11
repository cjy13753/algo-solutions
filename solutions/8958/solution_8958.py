num_testcases = int(input())
testcases = []
for i in range(num_testcases):
    testcases.append(input())

def solution(testcases: list) -> None:
    for testcase in testcases:
        score = 0
        total = 0
        for c in testcase:
            if c == 'O':
                score +=1
                total += score
            else:
                score = 0
        print(total)

solution(testcases)