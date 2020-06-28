#   Reconstruct Itinerary

'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
'''


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dfs solution
        result = []
        mapping = {}
        stack = ["JFK"]

        for i in tickets:
            if i[0] in mapping:
                mapping[i[0]].append(i[1])
            else:
                mapping[i[0]] = [i[1]]

        for i in mapping:
            mapping[i].sort()

        while stack:
            curr = stack[-1]
            if curr in mapping and mapping[curr]:
                stack.append(mapping[curr].pop(0))
            else:  # leaf node
                result.append(stack.pop())

        return result[::-1]
