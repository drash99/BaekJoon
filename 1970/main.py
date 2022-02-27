n = int(input())

hyuns = []

dp = dict()

brands = list(map(int, input().split()))
tmpset = [[] for _ in range(101)]
for idx, i in enumerate(brands):
    for j in tmpset[i]:
        hyuns.append((j, idx+1))
    tmpset[i].append(idx+1)

def isin(hyun1, hyun2): # -1 for outside, 1 for inside, 0 for invalid
    h1s = hyun1[0]
    h1l = hyun1[1]
    h2s = hyun2[0]
    h2l = hyun2[1]
    if h2s <= h1s:
        if h2l <= h1l and h2l >= h1s:
            return 0
    else:
        if h2l >= h1l and h2s <= h1l:
            return 0
    if h1s <h2s<h1l:
        return 1
    else:
        return -1

def findmax(hyuns):
    if len(hyuns) <= 1:
        return len(hyuns)
    if hyuns in dp.keys():
        return dp[hyuns]
    if len(hyuns) == 2:
        if isin(hyuns[0], hyuns[1])!=0:
            dp[hyuns] = 2
            return 2
        else:
            dp[hyuns] = 1
            return 1
    maxv = 1
    for i in hyuns:
        ins = []
        outs = []
        for j in hyuns:
            if i!=j:
                isinr = isin(i,j)
                if isinr == 1:
                    ins.append(j)
                elif isinr == -1:
                    outs.append(j)
        maxv = max(findmax(tuple(ins)) + findmax(tuple(outs))+1, maxv)
    dp[hyuns] = maxv
    return maxv

print(findmax(tuple(hyuns)))
