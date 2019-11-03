"""
There are n islands connected by m boat rides. Each boat ride starts from island p and arrives at island q with a cost c.
Now given all the islands and boat rides, together with starting island src and the destination dst, find the least cost route from src to dst with up to t stops. (Note: number of stops is the number of island IN BETWEEN src and dst.). If there is no such route, output -1.
Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,700],[0,2,500],[]]
src = 0, dst = 2, t = 1
Output: 200
Explanation: 
The graph looks like this:
0 -> (100) 1 -> (100) 2 
0 -> (500) 2

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, t = 0
Output: 500
Explanation: 
The graph looks like this:
0 -> (100) 1 -> (100) 2 
0 -> (500) 2

"""

# print "Hello World"
import sys
def min_cost_route(src, dst, t, n, edges):
    
    if not edges or len(edges) == 0:
        return -1
        
    graph = generate_graph(edges)
    
    
    visit = set()
    visit.add(src)
    min_cost=[sys.maxsize]
    
    dfs(graph, src, dst, t + 1, 0, visit, min_cost)
    if min_cost[0] == sys.maxsize:
        return -1 
    return min_cost[0]

def generate_graph(edges):
    
    graph = {}
    
# edges = [[0,1,100],[1,2,100],[0,2,500]] -> { 0 : [1, 100], 
    
    for e in edges:
        new_src = e[0]
        new_dst_cost = [e[1], e[2]]
        if not new_src in graph.keys():
            graph[new_src] = []
        graph[new_src].append(new_dst_cost)
        
    return graph
    
    
def dfs(graph, src, dst, t, curr_cost, visit, min_cost):
   
    if t < 0:
        return
    if src == dst:
        # print("curr_cost={}, min_cost={}".format(curr_cost,min_cost))
        min_cost[0] = min(curr_cost, min_cost[0])
        # print("curr_cost={}, min_cost={}".format(curr_cost,min_cost))

        return
    
    next_step_list = graph[src]
    for step in next_step_list:
        print("step={}, curr_cost={}".format(step,curr_cost))
        new_src = step[0]
        new_cost = step[1]
        if not new_src in visit:
            visit.add(new_src)
            dfs(graph, new_src, dst, t - 1, curr_cost + new_cost, visit, min_cost)
            visit.remove(new_src)
    return
        
    
edges = [[0,1,100],[1,2,100],[0,2,100],[2,1,100],[0,1,400]]

print(generate_graph(edges))

# def min_cost_route(src, dst, t, n, edges):


print(min_cost_route(0, 3, 3, 3, edges))
