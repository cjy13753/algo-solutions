"""
    시간 복잡도 추론
    전체 for-loop 한 번 돌기 때문에 O(N)
    city.upper(): 도시 이름이 최대 20자이기 때문에 O(1)
    cache.remove(city): queue를 전체 탐색해야 하기 때문에 O(N)
    cache.append(city): queue이기 때문에 O(1)

    최악의 경우 O(N^2)의 풀이이다.
"""


from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    answer = 0
    cache = deque()
    
    for city in cities:
        city = city.upper()
        try:
            cache.remove(city)
            cache.append(city)
            answer += 1
        except:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
    
    return answer