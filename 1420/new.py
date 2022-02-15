import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
field = []
inf= 987654321

for i in range(n):
    field.append(list(input()))



edges = [0 for _ in range(n*m)] #self &1 up 2 down 4 left 8 right 16
flows = [0 for _ in range(5*n*m)] # edge+ (n*m) * 0: self 1:up 2d3l4r

for i in range(n):
    for j in range(m):
        if field[i][j] == 'K':
            source = i*m+j
        elif field[i][j] == 'H':
            sink = i*m+j
        
        if field[i][j] != '#':
            edges [i*m+j] = 1
            flows[i*m+j] = 1
            if i-1 >=0 and field[i-1][j] != '#':
                edges[i*m+j] |= 1
                flows[i*m+j] = 0
            if i+1 < n and field[i+1][j] != '#':
                edges[i*m+j] |= 2
                flows[i*m+j] = 0
            if j-1 >= 0 and field[i][j-1] != '#':
                edges[i*m+j] |= 4
                flows[i*m+j] = 0
            if j+1 < m and field[i][j+1] != '#':
                edges[i*m+j] |= 8
                flows[i*m+j] = 0

level = [-1 for _ in range(2*n*m)]
level[source] = 0

blockflow = [[] for _ in range(n*m)]



def leveling():
    targets = set()
    target = source
    assert level[target] >=0

    for edge in edges[target]:
        if (level[edge[0]] == -1 or level[edge[0]] - level[target] == 1) and edge[1] > edge[2]:
            blockflow[target].append(edge)
            level[edge[0]] = level[target]+1
            targets.add(edge[0])
    while(len(targets) != 0):
        newtargets= set()
        for target in targets:
            for edge in edges[target]:
                if (level[edge[0]] == -1 or level[edge[0]] - level[target] == 1) and edge[1] > edge[2]:
                    blockflow[target].append(edge)
                    level[edge[0]] = level[target]+1
                    newtargets.add(edge[0])
        targets = newtargets
    if level[sink] == -1:
        return False
    else:
        return True

def flowing(cursor, incoming, isvisit):
    possibleflow = incoming
    if cursor == sink:
        return incoming
    isvisit.add(cursor)

    for edge in blockflow[cursor]:
        if (edge[1] > edge[2] and possibleflow > 0 and edge[0] not in isvisit):
            flow = flowing(edge[0], min(possibleflow, edge[1]-edge[2]), isvisit)
            edge[2] += flow
            for backedge in edges[edge[0]]:
                if backedge[0] == cursor:
                    backedge[2] -= flow
                    break
            possibleflow -= flow
    assert incoming >= possibleflow
    return incoming-possibleflow


while leveling():
    isvisit = set()
    flowing(source, inf, isvisit)
    level = [-1 for _ in range(n*m)]
    level[source] = 0
    blockflow = [[] for _ in range(n*m)]



ans = 0
fail = False
for edge in edges[source]:
    ans += edge[2]
    if edge[0] == sink:
        fail = True
        print(-1)

if not fail:
    print(ans)

    