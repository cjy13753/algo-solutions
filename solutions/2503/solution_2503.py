import sys
from itertools import permutations

def solution(guesess_and_answers: list) -> None:
    count = 0
    for candidate in permutations([chr(ord('1') + i) for i in range(9)], 3):
        flag = True
        for guess_and_answer in guesess_and_answers:
            guess_strike = guess_and_answer[1]
            guess_ball = guess_and_answer[2]
            candidite_strike_against_guess = 0
            candidite_ball_against_guess = 0
            guess = guess_and_answer[0]

            for i in range(3):
                if guess[i] == candidate[i]:
                    candidite_strike_against_guess += 1
                elif guess[i] in candidate:
                    candidite_ball_against_guess += 1
            
            if guess_strike != candidite_strike_against_guess:
                flag = False
                break
            
            if guess_ball != candidite_ball_against_guess:
                flag = False
                break
        
        if flag == True:
            count += 1
    
    print(count)

n = int(sys.stdin.readline())
guesses_and_answers = []
for _ in range(n):
    guess, strike, ball = sys.stdin.readline().split()
    guesses_and_answers.append([list(guess), int(strike), int(ball)])

solution(guesses_and_answers)