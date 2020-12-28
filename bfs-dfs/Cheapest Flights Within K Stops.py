"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

Solution : BFS with pruning. Keep exploring all flights till K stops. Explore only less expensive paths, if you already have an answer.
           If you are at last flight, only explore the flight to the destination.
           Create a hashmap with outgoing flights to lookup options at each point.
           Create a queue for processing the flights.

           Time complexity :If V -> vertices E-> edges
                                V*E -> no of connections between them.
                                K -> no of stops allowed
                            then E*K is time complexity. 
            Space complexity : V*K for queue. and V*E for dictionary to store graph


     TODO Dijstkstras / Bellman Ford
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        #bfs
        flights_queue = collections.deque()
        flights_graph = {}
        for s,d,p in flights:
            if s == src:
                flights_queue.append([s,d,p])
            flights_graph[s] = flights_graph.get(s, []) + [[d,p]]
        #print(flights_queue)
        #print(flights_graph)
        ans = -1
        stops = 0
        while flights_queue and stops <= K:
            for _ in range(len(flights_queue)):
                s,d,p = flights_queue.popleft()
                #print(stops, s,d,p)
                if d == dst:
                    if ans == -1:
                        ans = p
                    elif ans > p:
                        ans = p
                if d in flights_graph:
                        for dest,price in flights_graph[d]:
                            #prune last paths
                            if stops < K or (stops == K and dest==dst):
                                #go to this path only if it is less expensive
                                #prune more expensive paths
                                if ans==-1 or (ans > p+price):
                                    flights_queue.append([d,dest,p+price])
            stops+=1
        return ans