import sys
inf = 987654321

n,p = map(int, input().split())

edges = [[] for _ in range(n)]

for _ in range(p):
    s, e = map(int, sys.stdin.readline().split())
    edges[s-1].append([e-1,1,0])
    edges[e-1].append([s-1,0,0])


sink = 1
level = [-1 for _ in range(n)]
level[0] = 0

blockflow = [[] for _ in range(n)]

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
    level = [-1 for _ in range(n)]
    level[0] = 0
    blockflow = [[] for _ in range(n)]



ans = 0
for edge in edges[0]:
    ans += edge[2]
"""
for edge in edges:
    print(edge)"""
print(ans)

