

0,1,2,3,4,5

def max_window(nums, k):

    window = []
    res = []

    for idx, x in enumerate(nums):

        if idx >= k and window[0] <= idx - k:
            window.pop(0)
        while window and nums[window[-1]] <= x:
            window.pop()

        window.append(idx)
        if idx > k - 1:
            res.append(nums[window[0]])

    return res

if __name__ == "__main__":

    test1 = [2,3,1,4,5,2,1,6,7]
    print(max_window(test1, 3))

    a = 100 
    print(a)


    
