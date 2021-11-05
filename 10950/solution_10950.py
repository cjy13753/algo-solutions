num_testcases = int(input())
testcases = []
for i in range(num_testcases):
    testcase = list(map(int, input().split()))
    testcases.append(testcase)

def solution(testcases: list) -> None:
    for testcase in testcases:
        print(testcase[0] + testcase[1])

solution(testcases)