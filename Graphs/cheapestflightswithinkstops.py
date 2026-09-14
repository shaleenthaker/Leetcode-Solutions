"""There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1."""

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0
        for i in range(k + 1):
            curr = costs.copy()
            for flight in flights:
                costs[flight[1]] = min(costs[flight[1]], curr[flight[0]] + flight[2])
        return costs[dst] if costs[dst] != float('inf') else -1

