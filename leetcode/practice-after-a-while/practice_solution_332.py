from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        itinerary = []
        targets = {}
        for src, dst in tickets:
            if src not in targets:
                targets[src] = []
            targets[src].append(dst)

        def dfs(startCity: str) -> bool:
            itinerary.append(startCity)

            if startCity not in targets:
                if len(itinerary) -1 == len(tickets):
                    return True
                else:
                    return False
            else:
                if len(targets[startCity]) == 0:
                    if len(itinerary) -1 == len(tickets):
                        return True
                    else:
                        return False
                else:
                    for idx, arriveCity in enumerate(targets[startCity]):
                        targets[startCity].remove(arriveCity)                        
                        if dfs(arriveCity):
                            return True
                        targets[startCity].insert(idx, arriveCity)
                        itinerary.pop()
                    return False

        dfs("JFK")
        return itinerary

print(Solution().findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))