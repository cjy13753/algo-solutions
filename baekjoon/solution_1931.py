import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numMeetings = int(input())
        meetings = []
        for _ in range(numMeetings):
            meetings.append(list(map(int, input().split())))
        
        self.maximumMeetings(meetings)

    def maximumMeetings(self, meetings: list):
        meetings.sort(key=lambda x: (x[1], x[0]))
        lastMeetingEndTime = 0
        cnt = 0
        for start, end in meetings:
            if lastMeetingEndTime <= start:
                cnt += 1
                lastMeetingEndTime = end

        print(cnt)

Solution()