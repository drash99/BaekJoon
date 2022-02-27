import heapq

def prim_algorithm(adj):
    n = len(adj)
    output = 0
    
    notvisit = set(range(1, n))
    tmpedges = []
    for j in adj[0]:
        heapq.heappush(tmpedges, (j[1], j[0]))
    while len(notvisit) > 0:
        minimu = heapq.heappop(tmpedges)
        while not minimu[1] in notvisit:
            minimu = heapq.heappop(tmpedges)
        output += minimu[0]
        notvisit.remove(minimu[1])

        for j in adj[minimu[1]]:
            if j[0] in notvisit:
                heapq.heappush(tmpedges, (j[1], j[0]))

    return output

v,e = map(int,input().split())
adjmat = [[] for _ in range(v)]

for _ in range(e):
    a,b,c = map(int,input().split())
    adjmat[a-1].append((b-1,c))
    adjmat[b-1].append((a-1,c))


mst = prim_algorithm(adjmat)
print(mst)