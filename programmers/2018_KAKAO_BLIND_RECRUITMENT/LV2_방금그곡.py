""" 
Attempt #1

1시간 소요, 실패
"""

from collections import Counter

def solution(m, musicinfos):
    answer = ''
    playedTime = 0
    
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        endHour = int(end[:2])
        startHour = int(start[:2])
        endMinute = int(end[3:])
        startMinute = int(start[3:])
        durationReal = (endHour - startHour) * 60 + (endMinute - startMinute)
        counter = Counter(melody)
        durationOriginal = sum(counter.values()) - counter['#']
        q, r = divmod(durationReal, durationOriginal)
        modifiedMelody = melody * q + melody[:r]
        
        index = modifiedMelody.find(m)
        
        if index != -1:
            if index + len(melody) >= len(modifiedMelody):
                if durationReal > playedTime:
                    answer = title
            else:
                if modifiedMelody[index + len(melody)] != '#':
                    if durationReal > playedTime:
                        answer = title
            
    if answer == '':
        return "(None)"
    return answer