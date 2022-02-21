f,p = map(int, input().split())


#0 :source, 1~n : person n+1~n+d: food #len(alphas)-1: sink

edges = [[] for _ in range(len(alphas))] #target, 

def alphatoidx(alpha):
    return alphas.index(alpha)

for i in range(1,n+1):
    raw = sys.stdin.readline().strip().split()
    s = alphatoidx(raw[0])
    e = alphatoidx(raw[1])
    f = int(raw[2])
    edges[s].append([e,f,0])
    edges[e].append([s,f,0])

"""n = 2
d = 2
edges = [[[1,10,0],[2,10,0]],[[3,4,0],[4,8,0],[2,2,0]],[[4,9,0]],[[5,10,0]],[[3,6,0],[5,10,0]],[]]
"""
sink = len(alphas)-1
level = [-1 for _ in range(len(alphas))]
level[0] = 0

blockflow = [[] for _ in range(len(alphas))]

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
    level = [-1 for _ in range(len(alphas))]
    level[0] = 0
    blockflow = [[] for _ in range(len(alphas))]


ans = 0
for edge in edges[0]:
    ans += edge[2]


print(ans)
