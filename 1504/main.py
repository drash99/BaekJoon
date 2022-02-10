import heapq
import sys

v,e = map(int, input().split())

inf = 987654321


adjdic = dict()

for i in range(e):
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

oil1, oil2 = map(int,input().split())

def finddest(src,dest):
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
    
    return dijkmat[dest]


way1 = finddest(1, oil1)
way2 = finddest(oil1, oil2)
way3 = finddest(oil2, v)
way4 = finddest(1, oil2)
way5 = finddest(oil1, v)



if way1+way3 > way4+way5:
    if way4+way5+way2 >= inf:
        print(-1)
    else:
        print(way4+way5+way2)
else:
    if way1+way3+way2 >= inf:
        print(-1)
    else:
        print(way1+way3+way2)


