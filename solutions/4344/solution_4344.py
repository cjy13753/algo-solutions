num_testcases = int(input())
testcases = []
for i in range(num_testcases):
    testcases.append(input().split())

def solution(testcases: list) -> None:
    for testcase in testcases:
        num_students = int(testcase[0])
        score_list = list(map(int, testcase[1:]))
        avg = sum(score_list) / num_students
        num_above_avg = 0

        for score in score_list:
            if (score > avg):
                num_above_avg += 1
        
        rate_above_avg = num_above_avg / num_students * 100
        
        print(f"{rate_above_avg:.3f}%")

solution(testcases)