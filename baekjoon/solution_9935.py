import sys

given = "mirkovC4nizCC44"

bomb = "C4"


def recur(given) -> str:
    start = 0
    end = len(given) - 1
    numBomb = len(bomb)

    if len(given) < numBomb:
        return given
    if len(given) == numBomb:
        if given == bomb:
            return ""
        else:
            return given
    mid = start + (end - start) // 2
    left = recur(given[:mid])
    right = recur(given[mid:])

    concat = left + right
    count = -1
    while count != 0:
        i = 0
        count = 0
        while i < len(concat):
            if concat[i] == bomb[0]:
                j = i
                cFlag = True
                while j - i < numBomb:
                    if given[j] != bomb[j - i]:
                        cFlag = False
                        break
                    j += 1
                if cFlag == True:
                    count += 1
                    concat = concat[:j] + concat[j + numBomb - 1:]
            i += 1

    return concat


print(recur(given))