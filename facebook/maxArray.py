arr =[1,2,3,5,4,10,11,12,1,2,3,4,5,1,7,8,9,10,11,12,2,3,4,6]


# 1. if continue increase
#         curr++
#         update maxLen

#     if not continue increase:
#         can skip
#             startID = i
#             if i + 2 < len
#                 i = i + 2
#             else:
#                 break
#             curr += 1
#             update skip
#         else:

def maxArr(nums):

    maxLen = 1
    curr = 1
    skipped = False
    
    i = 1
    for i in range(1, len(nums)):
        if (nums[i] > nums[i - 1]):
            print("curr={},nums[i]={}, max={}, i ={}".format(curr,nums[i],maxLen, i))

            curr += 1
            maxLen = max(maxLen, curr)

        else:
            if not skipped:
                if i + 1 < len(nums) and nums[i + 1] > nums[i]:
                    skipped = True
                    startIdx = i
                    maxLen = max(maxLen, curr)
                else:
                    curr = 1

            else:
                i = startIdx
                curr = 1
                skipped = False

    return maxLen

print(maxArr(arr))



        

        



