import sys

def print_all_test_cases(cases: list) -> None:
    ans = []
    for case in cases:
        res = []
        find_all_lotto_cases(case, res)
        ans.append("\n".join(res))
    print("\n\n".join(ans))


def find_all_lotto_cases(start: list, res: list, end: list = []) -> None:
    if len(start) + len(end) < 6:
        return
    if len(end) == 6:
        res.append(" ".join(end))
        return
    for i in range(len(start)):
        find_all_lotto_cases(start[i+1:], res, end + start[i:i+1])


stopper = -1
cases = []
while stopper != 0:
    case_raw = list(sys.stdin.readline().split())
    case_size = int(case_raw[0])
    if case_size == 0:
        stopper = 0
        continue
    case_nums = case_raw[1:]
    cases.append(case_nums)

print_all_test_cases(cases)