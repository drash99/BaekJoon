import sys
inf = 987654321

n,k,d = map(int, input().split())

#0 :source, 1~n : person n+1~n+d: food #n+d+1: sink

edges = [[] for _ in range(n+d+2)] #target, 
ds = list(map(int, input().split()))
for i in range(1,n+1):
    edges[0].append([i,k,0])
    edges[i].append([0,0,0])
    avail = map(int, sys.stdin.readline().split()[1:])
    for j in avail:
        edges[i].append([j+n,1,0])
        edges[j+n].append([i,0,0])

for i in range(n+1, n+d+1):
    edges[i].append([n+d+1,ds[i-n-1],0])
    edges[n+d+1].append([i,0,0])

"""n = 2
d = 2
edges = [[[1,10,0],[2,10,0]],[[3,4,0],[4,8,0],[2,2,0]],[[4,9,0]],[[5,10,0]],[[3,6,0],[5,10,0]],[]]
"""
sink = n+d+1
level = [-1 for _ in range(n+d+2)]
level[0] = 0

blockflow = [[] for _ in range(n+d+2)]

def leveling():
    targets = set()
    target = 0
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

def flowing(cursor, incoming):
    possibleflow = incoming
    if cursor == sink:
        return incoming

    for edge in blockflow[cursor]:
        if (edge[1] > edge[2] and possibleflow > 0 ):
            flow = flowing(edge[0], min(possibleflow, edge[1]-edge[2]))
            edge[2] += flow
            for backedge in edges[edge[0]]:
                if backedge[0] == cursor:
                    backedge[2] -= flow
                    break
            possibleflow -= flow
    assert incoming >= possibleflow
    return incoming-possibleflow



while leveling():
    flowing(0, inf)
    level = [-1 for _ in range(n+d+2)]
    level[0] = 0
    blockflow = [[] for _ in range(n+d+2)]


ans = 0
for edge in edges[0]:
    ans += edge[2]

print(ans)
