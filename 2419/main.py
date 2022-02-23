n, m = map(int,input().split())

lefts = [0]
rights = [0]

inf = 987654321

dpl = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
dpr = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]


ans = 0
for _ in range(n):
    tmp = int(input())
    if tmp < 0:
        lefts.append(tmp)
    elif tmp > 0:
        rights.append(tmp)
    else:
        ans += m
lefts.sort(key=lambda x: -x)
rights.sort()
dpl[0][0] = (0,0)
dpr[0][0] = (0,0)
for i in range(1,n+1):
    for j in range(0, i+1):
        if j < len(lefts) and i-j < len(rights):
            #print(j,i-j)
            if j> 0:
                if dpl[j-1][i-j][0]-lefts[j]+lefts[j-1]-dpl[j-1][i-j][1] < dpr[j-1][i-j][0]+rights[i-j]-lefts[j]-dpr[j-1][i-j][1] :
                    a = dpl[j-1][i-j][0] -lefts[j]+lefts[j-1]
                    b = max(0, m-(dpl[j-1][i-j][0] -lefts[j]+lefts[j-1]))+ dpl[j-1][i-j][1]
                    dpl[j][i-j] = (a,b)
                else:
                    a = dpr[j-1][i-j][0] -lefts[j]+rights[i-j]
                    b = max(0, m-(dpr[j-1][i-j][0] -lefts[j]+rights[i-j]))+ dpr[j-1][i-j][1]
                    dpl[j][i-j] = (a,b)
            if i-j> 0:
                if dpr[j][i-j-1][0]+rights[i-j]-rights[i-j-1]-dpr[j][i-j-1][1]  < dpl[j][i-j-1][0]-lefts[j]+rights[i-j]-dpl[j][i-j-1][1] :
                    a = dpr[j][i-j-1][0]+rights[i-j]-rights[i-j-1] 
                    b = max(0, m-(dpr[j][i-j-1][0]+rights[i-j]-rights[i-j-1]))+ dpr[j][i-j-1][1]
                    #print(a,b,'hi')
                    dpr[j][i-j] = (a,b)
                else:
                    a = dpl[j][i-j-1][0]-lefts[j]+rights[i-j]
                    b = max(0, m-(dpl[j][i-j-1][0] -lefts[j]+rights[i-j]))+ dpl[j][i-j-1][1]
                    dpr[j][i-j] = (a,b)

print(ans + max(dpl[len(lefts)-1][len(rights)-1][1], dpr[len(lefts)-1][len(rights)-1][1] ))

