'''
Attempt #1:PASS

Time spent: 31m
My own answer: yes

Time complexity:
O(NlogN), N은 총 노래 개수
N개의 노래를 maxheap에 넣느라 O(NlogN)
total_per_genre 정렬하느라 O(NlogN)

Space complexity:
O(N), defaultdict에 노래 넣어야 해서
'''

import heapq
from collections import defaultdict

def solution(genres, plays):
    answer = []
    MAX_SONGS_PER_GENRE = 2

    total_per_genre = defaultdict(int) # {genre: total_count}
    maxheap_per_genre = defaultdict(list) # {genre: max_heap}, max_heap = [(-play_count, song_id)]

    for i in range(len(genres)):
        total_per_genre[genres[i]] += plays[i]
        heapq.heappush(maxheap_per_genre[genres[i]], (-plays[i], i))
    
    result = list(total_per_genre.items())
    result.sort(key=lambda x:(x[1]), reverse=True)

    for genre, _ in result:
        max_heap = maxheap_per_genre[genre]
        count = 0
        while max_heap and count < MAX_SONGS_PER_GENRE:
            count += 1
            _, song_id = heapq.heappop(max_heap)
            answer.append(song_id)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))