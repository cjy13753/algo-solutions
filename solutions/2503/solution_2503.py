import sys
from itertools import permutations

def solution(guesses_and_results: list) -> None:
    count = 0
    candidates = permutations(list(range(1, 10)), 3)

    for candidate in candidates:
        if validate(candidate, guesses_and_results):
            count += 1

    print(count)

def validate(candidate, guesses_and_results):
    for guess_and_result in guesses_and_results:
        guess, guess_strike, guess_ball = [*guess_and_result]
        candidite_strike_against_guess, candidite_ball_against_guess = 0, 0

        for i in range(3):
            if int(guess[i]) == candidate[i]:
                candidite_strike_against_guess += 1
            elif int(guess[i]) in candidate:
                candidite_ball_against_guess += 1
        
        if guess_strike != candidite_strike_against_guess or guess_ball != candidite_ball_against_guess:
            return False

    return True

n = int(sys.stdin.readline())
guesses_and_results = []
for _ in range(n):
    guess, strike, ball = sys.stdin.readline().split()
    guesses_and_results.append((guess, int(strike), int(ball)))

solution(guesses_and_results)