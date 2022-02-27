import heapq




def prim_algorithm(adj):
    # Implement here. Feel free to edit or remove the following two lines.
    n = len(adj)
    output = 0
    #output = [[False] * n for _ in range(n)]
    
    notvisit = set(range(1, n))
    tmpedges = []
    for j in notvisit:
        if adj[0][j] > 0:
            heapq.heappush(tmpedges, (adj[0][j], (0, j)))
    while len(notvisit) > 0:
        minimu = heapq.heappop(tmpedges)
        while not minimu[1][1] in notvisit:
            minimu = heapq.heappop(tmpedges)
        minimum = minimu[1]
        output += minimu[0]
        #output[minimum[1]][minimum[0]] = True
        #output[minimum[0]][minimum[1]] = True
        notvisit.remove(minimum[1])
        for j in notvisit:
            if adj[minimum[1]][j] > 0:
                heapq.heappush(tmpedges, (adj[minimum[1]][j], (minimum[1], j)))

    return output

v,e = map(int,input().split())
adjmat = [[0 for _ in range(v)] for _ in range(v)]

for _ in range(e):
    a,b,c = map(int,input().split())
    adjmat[a-1][b-1] = c

mst = prim_algorithm(adjmat)
print(mst)