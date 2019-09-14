# import queue

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:

#         sorted_list_head = sorted_list_tail = ListNode(0)
        
#         pq = queue.PriorityQueue()
        
#         def add_node_in_pq(idx, node):
#             if node:
#                 pq.put((node.val, idx, node))
        
#         for idx, node in enumerate(lists):
#             add_node_in_pq(idx, node)
        
#         while not pq.empty():
#             _, idx, node = pq.get()
#             add_node_in_pq(idx, node.next)
#             node.next = None
#             sorted_list_tail.next = node
#             sorted_list_tail = sorted_list_tail.next
        
#         return sorted_list_head.next

import queue

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None



from queue import PriorityQueue

q = PriorityQueue()



class MyPriorityQueue:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other):
        if self.b == other.b:
            return self.c < other.c
        return self.b < other.b


q.put(MyPriorityQueue(1,1,3))
q.put(MyPriorityQueue(1,2,4))
q.put(MyPriorityQueue(1,2,3))
q.put(MyPriorityQueue(1,2,6))
q.put(MyPriorityQueue(1,3,1))
q.put(MyPriorityQueue(1,3,2))
q.put(MyPriorityQueue(1,6,3))


class MyNode:
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col
    

def mergeKsorted(lists):
    q = PriorityQueue()

    for i in range(len(lists)):
        
        if len(lists[i]) > 0:
            q.put((lists[i][0], i, 0))
    res = []
    while not q.empty():
        node = q.get()
        val, row, col = node[0], node[1], node[2]
        print("val={}, row={}, col={}".format(val,row,col))
        res.append(val)
        if col < len(lists[row]) - 1:
            q.put((lists[row][col + 1], row, col + 1))


    return res


arr =[
    [1,3,5,6,8,9],
    [2,3,6,7],
    [0,1,1]
]

print(mergeKsorted(arr))
        
