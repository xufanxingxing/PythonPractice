"""
give a list of pairs representing the relation of two contries.
find the largest size of all exiting relation group

eg:
[[a,b],[b,c],[r,f]] ->[[a,b,c],[r,f]] 

output should be 2:
"""


def contryMatch(pairs):
    graph = {}

    for pair in pairs:

        l0 = graph.get(pair[0], [])
        l0.append(pair[1])
        graph[pair[0]] = l0

        l1 = graph.get(pair[1], [])
        l1.append(pair[0])
        graph[pair[1]] = l1
    print(graph)
    
    visit = set()
    maxSize = 0
    for contry in graph.keys():

        maxSize = max(maxSize, dfs(graph, visit, contry))
    return maxSize


def dfs(graph, visit, curr):
    
    if curr in visit:
        return 0
    visit.add(curr)
    size = 1
    for e in graph[curr]:
        size = size + dfs(graph, visit, e)
    return size
    

pairs = [['a','b'],['b','c'],['b','t'],['b','r'],['t','l'],['r','f'],['r','o']] 
print(contryMatch(pairs))



