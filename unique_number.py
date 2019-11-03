def unique_number(arr):
    curr = 0
    for v in arr:
        curr = curr ^ v

    return curr

arr = [1,1,2,2,3,3,4,5,5]
print(unique_number(arr))


def move_zeno(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            i += 1

    return arr

arr2 = [0,0,1,2,0,3,0,0,4,5,0]
print(move_zeno(arr2))
        

