n, m = map(int,input().split())

lefts = [0]
rights = [0]

inf = 987654321

dpl = [[(inf, 0, inf) for _ in range(n+1)] for _ in range(n+1)]
dpr = [[(inf, 0, inf) for _ in range(n+1)] for _ in range(n+1)]


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
anstmp = 0
maxi= 0
for l in range(len(lefts)+len(rights)):
    k = l+1
    #maxi= 0
    for i in range(1,n+1):
        for j in range(0, i+1):
            if j < len(lefts) and i-j < len(rights):
                #print(j,i-j)

                if j> 0:
                    
                    if dpl[j-1][i-j][2]+(k-i)*(-lefts[j]+lefts[j-1]) < dpr[j-1][i-j][2]+(k-i)*(rights[i-j]-lefts[j]):
                        a = -lefts[j]+lefts[j-1]
                        b = max(0, m-a)+ dpl[j-1][i-j][1]
                        c = dpl[j-1][i-j][2] + (k-i)*a
                        #print('hi')
                    else:
                        a = -lefts[j]+rights[i-j]
                        b = max(0, m-a)+ dpr[j-1][i-j][1]
                        c = dpr[j-1][i-j][2] + (k-i)*a
                    dpl[j][i-j] = (a,b,c)
                if i-j> 0:
                    #print(dpr[j][i-j-1])
                    #print(dpl[j][i-j-1])
                    #print(dpr[j][i-j-1][2]+min(m,dpr[j][i-j-1][0]+rights[i-j]-rights[i-j-1]))
                    #print(dpl[j][i-j-1][2]+min(m, dpl[j][i-j-1][0]-lefts[j]+rights[i-j]))
                    if dpr[j][i-j-1][2]+(k-i)*(rights[i-j]-rights[i-j-1]) < dpl[j][i-j-1][2]+(k-i)*(-lefts[j]+rights[i-j]):
                        a = rights[i-j]-rights[i-j-1]
                        b = max(0, m-a)+ dpr[j][i-j-1][1]
                        c = dpr[j][i-j-1][2] + (k-i)*a
                        #print('hi2')
                        #rint(a,b,'hi')
                    else:
                        a = -lefts[j]+rights[i-j]
                        b = max(0, m-a)+ dpl[j][i-j-1][1]
                        c = dpl[j][i-j-1][2] + (k-i)*a
                    dpr[j][i-j] = (a,b,c)
                #print(a,b,c, i,j)

    for j in range(0, n+1):
        if j < len(lefts) and l-j < len(rights):
            #print(j,l-j, 'hi', dpl[j][l-j][2], dpr[j][l-j][2])
            maxi = max(maxi, l*m-dpl[j][l-j][2])
            maxi = max(maxi, l*m-dpr[j][l-j][2])
    #print(maxi,l)
#print(dpl)
#print(dpr)

print(ans + maxi)

