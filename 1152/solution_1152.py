senetence = input()

def solution(sentence: str) -> None:
    num_words = 0
    index = 0
    is_prev_char = False
    while index < len(senetence):
        if senetence[index] == " ":
            is_prev_char = False
        else:
            if is_prev_char == False:
                num_words += 1
                is_prev_char = True
        index += 1
    
    print(num_words)

solution(senetence)