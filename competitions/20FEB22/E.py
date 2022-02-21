n, m = map(int, input().split())
mapk = [[0 for _ in range(m)] for _ in range(n)]



for i in range(n):
    for idx, j in enumerate(map(int, input().split())):
        if j == -1:
            mapk[i][idx] = 1
        elif j == 1:
            src = (i, idx)
            mapk[i][idx] = 1
        elif j == 2:
            dest = (i, idx)
            mapk[i][idx] = 1
inf = 987654321

mapsrc = [[inf for _ in range(m)] for _ in range(n)]

mapdest = [[inf for _ in range(m)] for _ in range(n)]

mapsrc[src[0]][src[1]] = 0
step = 0
watching = set()
if src[1]+1<m and mapk[src[0]][src[1]+1] == 0:
    watching.add((src[0],src[1]+1))
if src[1]>0 and mapk[src[0]][src[1]-1] == 0:
    watching.add((src[0],src[1]-1))

if src[0]+1<n and mapk[src[0]+1][src[1]] == 0:
    watching.add((src[0]+1,src[1]))
if src[0]>0 and mapk[src[0]-1][src[1]] == 0:
    watching.add((src[0]-1,src[1]))


mapdest[dest[0]][dest[1]] = 0
step = 0
watching2 = set()
if dest[1]+1<m and mapk[dest[0]][dest[1]+1] == 0:
    watching2.add((dest[0],dest[1]+1))
if dest[1]>0 and mapk[dest[0]][dest[1]-1] == 0:
    watching2.add((dest[0],dest[1]-1))

if dest[0]+1<n and mapk[dest[0]+1][dest[1]] == 0:
    watching2.add((dest[0]+1,dest[1]))
if dest[0]>0 and mapk[dest[0]-1][dest[1]] == 0:
    watching2.add((dest[0]-1,dest[1]))

while len(watching) >0 or len(watching2) > 0:
    step+=1
    willwatch = set()
    for i in watching:
        mapsrc[i[0]][i[1]] = step
        if i in watching2:
            mapk[i[0]][i[1]] == 1
            continue
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
        mapk[i[0]][i[1]] == 1
    watching = willwatch
    willwatch = set()
    for i in watching2:
        mapdest[i[0]][i[1]] = step
        if step == mapsrc[i[0]][i[1]]:
            mapk[i[0]][i[1]] == 1
            continue
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
        mapk[i[0]][i[1]] == 1
    watching2 = willwatch

ans1 = 0
ans2 = 0
ans3 = 0

for i in range(n):
    for j in range(m):
        if mapsrc[i][j] >= inf and mapdest[i][j] >= inf:
            continue
        if mapsrc[i][j] > mapdest[i][j]:
            ans2+=1
        elif mapsrc[i][j] < mapdest[i][j]:
            ans1+=1
        else:
            ans3+=1


    
print(' '.join(map(str, [ans1, ans2, ans3])))