"""
input: a list of amazon user Browsing history， 
[userID， pageID，time]
[12,1,12/3]


find the 3 continues page id woth the maximum browsing frequency 


"""
from functools import cmp_to_key

def comp(x, y):
    if x['b'] == y['b']:
        return x['c'] - y['c']
    else: 
        return x['c'] - y['c']
    


arr = [{'a':"sth",'b':1,'c':2},{'a':"no",'b':1,'c':0},{'a':"sth",'b':2,'c':1},]


res = sorted(arr, key = cmp_to_key(comp))

print(res)


def comp(x,y):
    if x[0] -- y[0]:
        return x[1] - y[1]
    else:
        return x[0] - y[0]


sorted(arr, key = cmp_to_key(comp))
  

