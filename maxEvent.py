"""

a list of event with start time and end time. 
determine the maximum number of events that can be taken by one person

hint: greedy

[[1,4],[2,3],[5,8],[9,12]]
"""

import operator
def maxEvent(events):
    if not events or len(events) == 0:
        return 0

    endList = sorted(events, key = lambda x : x[1])
    count = 1
    currEnd = endList[0][1]
    for event in endList:
        if event[0] > currEnd:
            count += 1
            currEnd = event[1]

    return count


if __name__ == "__main__":

    a = [[1,8],[2,10],[5,8],[9,12]]

    print(maxEvent(a))

        


