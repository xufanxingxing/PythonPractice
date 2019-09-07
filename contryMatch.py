"""
give a list of pairs representing the relation of two contries.
find the largest size of all exiting relation group

eg:
[[a,b],[b,c],[r,f]] ->[[a,b,c],[r,f]] 

output should be 2:
"""

gmax = 0
def contryMatch(pairs):
    graph = {}

    for pair in pairs:

        l0 = graph.get(pair[0], [])
        l0.append(pair[1])
        graph[pair[0]] = l0

        l1 = graph.get(pair[1], [])
        l1.append(pair[0])
        graph[pair[1]] = l1
    
    visit = set()

    for contry in graph.keys():
        size = [0]
        dfs(graph, visit, contry, size)


def dfs(graph, visit, curr, size):
    
    if curr in visit:
        return
    visit.add(curr)
    size[0] =size[0] + 1
    global gmax
    gmax = max(gmax, size[0])
    
    for e in graph[curr]:
        dfs(graph, visit, e, size)
    

pairs = [['a','b'],['b','c'],['b','t'],['t','l'],['r','f']] 
contryMatch(pairs)
print(gmax)


