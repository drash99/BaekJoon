n, m = map(int, input().split())
mapk = [[0 for _ in range(m)] for _ in range(n)]
walls = set()

for i in range(n):
    for idx, j in enumerate(list(input())):
        if j == '1':
            mapk[i][idx] = 1
            walls.add((i,idx))
inf = 987654321

mapsrc = [[inf for _ in range(m)] for _ in range(n)]

mapdest = [[inf for _ in range(m)] for _ in range(n)]

mapsrc[0][0] = 0
step = 0
watching = set()
if 1<n and mapk[0][1] == 0:
    watching.add((0,1))

if 1<m and mapk[1][0] == 0:
    watching.add((1,0))

while len(watching) >0:
    step+=1
    willwatch = set()
    for i in watching:
        mapsrc[i[0]][i[1]] = step
        if i[0]-1 >= 0:
            if mapk[i[0]-1][i[1]] == 0 and mapsrc[i[0]-1][i[1]] == inf:
                willwatch.add((i[0]-1,i[1]))
        if i[0]+1<n and mapk[i[0]+1][i[1]] == 0 and mapsrc[i[0]+1][i[1]] == inf:
            willwatch.add((i[0]+1,i[1]))
        if i[1]-1 >= 0:
            if mapk[i[0]][i[1]-1] == 0 and mapsrc[i[0]][i[1]-1] == inf:
                willwatch.add((i[0],i[1]-1))
        if i[1]+1<m and mapk[i[0]][i[1]+1] == 0 and mapsrc[i[0]][i[1]+1] == inf:
            willwatch.add((i[0],i[1]+1))
    watching = willwatch


mapdest[n-1][m-1] = 0
step = 0
watching = set()
if 1<n and mapk[n-2][m-1] == 0:
    watching.add((n-2,m-1))

if 1<m and mapk[n-1][m-2] == 0:
    watching.add((n-1,m-2))

while len(watching) >0:
    step+=1
    willwatch = set()
    for i in watching:
        mapdest[i[0]][i[1]] = step
        if i[0]-1 >= 0:
            if mapk[i[0]-1][i[1]] == 0 and mapdest[i[0]-1][i[1]] == inf:
                willwatch.add((i[0]-1,i[1]))
        if i[0]+1<n and mapk[i[0]+1][i[1]] == 0 and mapdest[i[0]+1][i[1]] == inf:
            willwatch.add((i[0]+1,i[1]))
        if i[1]-1 >= 0:
            if mapk[i[0]][i[1]-1] == 0 and mapdest[i[0]][i[1]-1] == inf:
                willwatch.add((i[0],i[1]-1))
        if i[1]+1<m and mapk[i[0]][i[1]+1] == 0 and mapdest[i[0]][i[1]+1] == inf:
            willwatch.add((i[0],i[1]+1))
    watching = willwatch

ans = mapdest[0][0]
for i in walls:
    fromsrc = inf
    fromdest = inf
    if i[0]-1 >= 0:
        if mapk[i[0]-1][i[1]] == 0:
            fromsrc = min(fromsrc, mapsrc[i[0]-1][i[1]])
            fromdest = min(fromdest, mapdest[i[0]-1][i[1]])
    if i[0]+1<n and mapk[i[0]+1][i[1]] == 0:
        fromsrc = min(fromsrc, mapsrc[i[0]+1][i[1]])
        fromdest = min(fromdest, mapdest[i[0]+1][i[1]])
    if i[1]-1 >= 0:
        if mapk[i[0]][i[1]-1] == 0:
            fromsrc = min(fromsrc, mapsrc[i[0]][i[1]-1])
            fromdest = min(fromdest, mapdest[i[0]][i[1]-1])
    if i[1]+1<m and mapk[i[0]][i[1]+1] == 0:
        fromsrc = min(fromsrc, mapsrc[i[0]][i[1]+1])
        fromdest = min(fromdest, mapdest[i[0]][i[1]+1])
    if ans > fromsrc + fromdest + 2:
        ans = fromsrc + fromdest + 2

if ans >= inf:
    print(-1)
else:
    print(ans+1)
