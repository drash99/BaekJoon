import heapq
import sys

v,e = map(int, input().split())
src = int(input())

inf = 987654321

dijkmat = [inf for _ in range(v+1)]
dijkmat[src] = 0

possible = [] # weight, source, target vertex
visited = set()
visited.add(src)
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

for i in range(1,len(dijkmat)):
    if dijkmat[i] == inf:
        print('INF')
    else:
        print(dijkmat[i])



