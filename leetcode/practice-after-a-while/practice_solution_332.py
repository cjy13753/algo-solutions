from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        itinerary = []
        numRemainingTickets = [len(tickets)]
        adjList = {}
        for departCity, arriveCity in tickets:
            if departCity not in adjList:
                adjList[departCity] = set()
            if arriveCity not in adjList:
                adjList[arriveCity] = set()
            adjList[departCity].add(arriveCity)

        def recur(departCity):
            itinerary.append(departCity)
            
            if len(adjList[departCity]) == 0:
                if numRemainingTickets[0] == 0:
                    if len(answer) == 0:
                        answer = itinerary
                    else:
                        if ''.join(itinerary) < ''.join(answer):
                            answer = itinerary
                return

            for arriveCity in list(adjList[departCity]):
                adjList[departCity].remove(arriveCity)
                numRemainingTickets[0] -= 1
                recur(arriveCity)
                itinerary.pop()
                adjList[departCity].add(arriveCity)
                numRemainingTickets[0] += 1

        recur("JFK")
        return answer

print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))