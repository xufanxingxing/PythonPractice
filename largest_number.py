def my_comp( a, b):
    if len(a) == len(b):
        return int(b) - int(a)
    
    i = 0
    length = min(len(a), len(b))
    
    for i in range(length):
        if int(a[i]) != int(b[i]):
            return int(b[i]) - int(a[i])
        
    if len(a) > len(b):
        return int(a[0]) - int(a[length])
    else:
        return int(b[0]) - int(b[length])


a = "123"
b = "1234"


print(my_comp( a, b))