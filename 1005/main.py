import sys

input = sys.stdin.readline

t = int(input())

def work(edges, watching,pt, time, timereq):
    ptcur = time[pt]-timereq[pt]
    for edge in edges[pt]:
        if edge[1] == 0:
            if time[edge[0]] == -1:
                #print(edge)
                return -1
            ptcur = max(ptcur, time[edge[0]])
        else:
            if not edge[0] in watching:
                watching.append(edge[0])
    return ptcur

for _ in range(t):
    n,k = map(int,input().split())
    edges = [[] for _ in range(n+1)]
    time = [-1 for _ in range(n+1)]
    timereq = list(map(int,input().split()))
    timereq.insert(0,0)
    starts = set(range(1,n+1))
    for _ in range(k):
        a,b = map(int, input().split())
        edges[a].append((b,1))
        edges[b].append((a,0))
        starts.discard(b)
    w = int(input())
    watching = list(starts)
    for node in starts:
        time[node] = timereq[node]
    cursor = 0
    while len(watching) > cursor:
        pt = watching[cursor]
        #print(pt, watching, time, timereq, edges)
        ptcur = work(edges, watching, pt, time, timereq)
        if ptcur>=0:
           time[pt] = timereq[pt]+ptcur
        else:
            watching.append(pt)
        cursor+=1
    #print(time)
    print(time[w])




