n, m = map(int,input().split())

lefts = [0]
rights = [0]

inf = 987654321

dpl = [[(inf,0,0) for _ in range(n+1)] for _ in range(n+1)]
dpr = [[(inf,0,0) for _ in range(n+1)] for _ in range(n+1)]


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
dpl[0][0] = (0,0,0)
dpr[0][0] = (0,0,0)
for i in range(1,n+1):
    for j in range(0, i+1):
        if j < len(lefts) and i-j < len(rights):
            print(j,i-j)
            if j> 0:
                if dpl[j-1][i-j][2]+dpl[j-1][i-j][0]-lefts[j]+lefts[j-1] < dpr[j-1][i-j][2]+dpr[j-1][i-j][0]+rights[i-j]-lefts[j]:
                    a = dpl[j-1][i-j][0] -lefts[j]+lefts[j-1]
                    b = max(0, m-a)+ dpl[j-1][i-j][1]
                    c = dpl[j-1][i-j][2] + a
                    dpl[j][i-j] = (a,b,c)
                else:
                    a = dpr[j-1][i-j][0] -lefts[j]+rights[i-j]
                    b = max(0, m-a)+ dpr[j-1][i-j][1]
                    c = dpr[j-1][i-j][2] + a
                    dpl[j][i-j] = (a,b,c)
            if i-j> 0:
                if dpr[j][i-j-1][2]+dpr[j][i-j-1][0]+rights[i-j]-rights[i-j-1] < dpl[j][i-j-1][2]+dpl[j][i-j-1][0]-lefts[j]+rights[i-j]:
                    a = dpr[j][i-j-1][0]+rights[i-j]-rights[i-j-1] 
                    b = max(0, m-a)+ dpr[j][i-j-1][1]
                    c = dpr[j][i-j-1][2] + a
                    #rint(a,b,'hi')
                    dpr[j][i-j] = (a,b,c)
                else:
                    a = dpl[j][i-j-1][0]-lefts[j]+rights[i-j]
                    b = max(0, m-a)+ dpl[j][i-j-1][1]
                    c = dpl[j][i-j-1][2] + a
                    dpr[j][i-j] = (a,b,c)

print(dpl[len(lefts)-1][len(rights)-1])
print(dpr[len(lefts)-1][len(rights)-1])
print(ans + max(dpl[len(lefts)-1][len(rights)-1][1], dpr[len(lefts)-1][len(rights)-1][1]) )

