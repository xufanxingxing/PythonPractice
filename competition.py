"""
list of result of competiton:
[[t1,t2],[t2,t3]...]
determine if tx can defeat  ty.

eg:
[[1,2],[2,3],[3,4]], 1, 4，
output: true

"""

def competition(results, t1, t2):
    graph = {}

    for res in results:
        l = graph.get(res[0], [])
        l.append(res[1])
        graph[res[0]] = l
    
    if not t1 in graph:
        return False
        
    canBeat = [False]

    search(graph, t1, t2, canBeat)

    return canBeat[0]
    

def search(graph, curr, end, canBeat):
    if curr == end:
        canBeat[0] = True
        return

    for team in graph[curr]:
        search(graph, team, end, canBeat)


teams = [[1,2],[2,3],[3,4]]

print(competition(teams, 4,1))