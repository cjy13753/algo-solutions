""" 
Attempt #2

해설에서 힌트 보고 substitution 사용해서 성공

시간 복잡도:
O((N-M)*M), M길이의 단어가 N길이의 단어에 존재하는지 찾기
왜냐하면 string in operator 사용
"""

from collections import Counter

def substitute(melody):
    temp = []
    for i in range(len(melody)):
        if melody[i] == '#':
            popped = temp.pop()
            temp.append(popped.lower())
        else:
            temp.append(melody[i])
    return ''.join(temp)


def solution(m, musicinfos):
    answer = "(None)"
    playedTime = 0

    m = substitute(m)
    
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        endHour = int(end[:2])
        startHour = int(start[:2])
        endMinute = int(end[3:])
        startMinute = int(start[3:])
        durationReal = (endHour - startHour) * 60 + (endMinute - startMinute)

        melody = substitute(melody)

        counter = Counter(melody)
        durationOriginal = sum(counter.values())
        q, r = divmod(durationReal, durationOriginal)
        modifiedMelody = melody * q + melody[:r]

        if m in modifiedMelody:
            if durationReal > playedTime:
                answer = title
                playedTime = durationReal
            
    return answer