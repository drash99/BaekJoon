import heapq
import sys
input = sys.stdin.readline

v, k = map(int, input().split())

inf = 987654321


adjdic = dict()

for i in range(v-1):
    a,b,c = map(int, sys.stdin.readline().split())
    if a in adjdic.keys():
        if b in adjdic[a].keys():
            adjdic[a][b] = min(adjdic[a][b], c)
        else:
            adjdic[a][b] = c
    else:
        adjdic[a] = {b:c}
    if b in adjdic.keys():
        if a in adjdic[a].keys():
            adjdic[b][a] = min(adjdic[b][a], c)
        else:
            adjdic[b][a] = c
    else:
        adjdic[b] = {a:c}



def finddest(src):
    dijkmat = [inf for _ in range(v+1)]
    dijkmat[src] = 0

    possible = [] # weight, source, target vertex
    visited = set()
    visited.add(src)
    if src in adjdic.keys():
        for i in adjdic[src].keys():
            dijkmat[i] = adjdic[src][i]
            heapq.heappush(possible, (adjdic[src][i], src, i))
    
    while(len(possible) > 0 and len(visited)!=v):
        todo = heapq.heappop(possible)
        if not todo[2] in adjdic.keys():
            continue
        for i in adjdic[todo[2]].keys():
            if dijkmat[i] > adjdic[todo[2]][i]+dijkmat[todo[2]]:
                dijkmat[i] = adjdic[todo[2]][i]+dijkmat[todo[2]]
            if not todo[2] in visited:
                heapq.heappush(possible, (adjdic[todo[2]][i]+dijkmat[todo[2]], todo[2], i))
        visited.add(todo[2])
    
    return dijkmat


for _ in range(k):
    s, e = map(int, input().split())
    mat1 = finddest(s)
    mat2 = finddest(e)
    ans = (0,inf)
    for i in range(1,v+1):
        if mat1[i] == mat2[i]:
            if ans[1] > mat1[i]:
                ans = (i, mat1[i])
    if ans[1] != inf:
        print((ans)[0])
    else:
        print(-1)



