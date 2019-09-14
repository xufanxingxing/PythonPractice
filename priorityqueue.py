from queue import PriorityQueue 

class MyNode:
    def __init__(self, arr):
        self.a = arr[0]
        self.b = arr[1]
        self.c = arr[2]

    def __lt__(self, other):
        if self.b == other.b:
            return self.c < other.c   
        return self.b < other.b


p = PriorityQueue()

arr =[
    [1,2,3],
    [2,2,1],
    [3,4,5],
    [2,2,5],
    [5,6,8],
    [5,7,9]
]

for i in arr:
    p.put(MyNode(i))

while not p.empty():
    node = p.get()
    print(node.a, node.b, node.c)
