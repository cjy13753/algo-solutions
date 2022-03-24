from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = [[]]
        itinerary = []
        numRemainingTickets = [len(tickets)]
        adjList = {}
        for departCity, arriveCity in tickets:
            if departCity not in adjList:
                adjList[departCity] = []
            adjList[departCity].append(arriveCity)

        def dfs(departCity):
            itinerary.append(departCity)
            
            if departCity not in adjList or len(adjList[departCity]) == 0:
                if numRemainingTickets[0] == 0:
                    if len(answer[0]) == 0:
                        answer[0] = itinerary[:]
                    else:
                        if ''.join(itinerary) < ''.join(answer[0]):
                            answer[0] = itinerary[:]
                return

            for arriveCity in list(adjList[departCity]):
                adjList[departCity].remove(arriveCity)
                numRemainingTickets[0] -= 1
                dfs(arriveCity)
                itinerary.pop()
                adjList[departCity].append(arriveCity)
                numRemainingTickets[0] += 1

        dfs("JFK")
        return answer[0]

print(Solution().findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))