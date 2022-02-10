import math
n = int(input())

possible = set([(i,j) for i in range(n) for j in range(n)])

dp = dict()


ans = 0

def findsafe(status, pos):
    tmp = set()
    for i in status:
        if i[0] == pos[0]:
            continue
        elif i[1] == pos[1]:
            continue
        elif i[0]-pos[0] == i[1]-pos[1]:
            continue
        elif pos[0]-i[0] == i[1]-pos[1]:
            continue
        else:
            tmp.add(i)
    return tmp

def placeq(status, recurse):
    if len(status) == 0:
        return 0
    key = (tuple(status),recurse)
    if key in dp.keys():
        return dp[key]
    if recurse == n-1:
        dp[key] = len(status)
        return len(status)
    tmp = 0
    for i in status:
        tmp += placeq(findsafe(status, i), recurse+1)
    dp[key] = tmp
    return tmp

print(placeq(possible, 0))