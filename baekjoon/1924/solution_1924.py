import sys

def find_day(x: int, y: int) -> None:
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    days_passed = 0
    for i in range(1, x):
        days_passed += days_in_month[i]
    days_passed += y

    print(days[days_passed % 7])

x, y = list(map(int, sys.stdin.readline().split()))
find_day(x, y)