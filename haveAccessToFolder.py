# - 知识点：    Tree    buildTree     bfs     unordered_map   

# Assumption：  folders 第一个是root    在之后的内容基于之前built的tree   
 
# Given a list folders        vector of pairs
# folders = { {“A”,” “} , {“B”,”A”}, {“C”,”A”}. {“D”, “C”}, {“E”,”C”}… }
# and given an access list of folders
# access  =     {“B”, ”D”}
 
# implement a API         bool   hasAccess (string name)
# for example       hasAccess (“A”) ==  True       hasAccess (“B”)  == false

from collections import deque

class folder_system:
    def __init__(self, folders, access):
        self.graph = {}
        self.access = access

        for pair in folders:
            child = pair[0]
            parent = pair[1]

            child_list = self.graph.get(parent,[])
            child_list.append(child)
            self.graph[parent] = child_list

    def has_access(self, folder):
        print(self.graph)
        visit = set()
        queue = deque()
        for fold in self.access:
            queue.append(fold)
        print(queue)
        while queue:

            curr = queue.popleft()
            if curr == folder:
                return True
            if curr in self.graph.keys():
                for child in self.graph[curr]:
                    if child not in visit:
                        queue.append(child)
                        visit.add(child)

        return False


folders = [["A",""],["B","A"],["C","A"],["D", "C"],["E","C"]]
access= ["C","D"]


folder_sys = folder_system(folders, access)

print(folder_sys.has_access("B"))





    

