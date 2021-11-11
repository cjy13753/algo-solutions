num_testcases = int(input())
testcases = []
for i in range(num_testcases):
    testcases.append(input().split())

def solution(testcases: list) -> None:
    for testcase in testcases:
        repeat = int(testcase[0])
        concat = ""
        for c in testcase[1]:
            concat += c * repeat
        print(concat)

solution(testcases)