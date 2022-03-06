import sys, os
from io import BytesIO, IOBase


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
#endregion



def dfs(notvisited, currentPosition, edges, tocolor, nodeColor):
    notvisited.remove(currentPosition)
    nodeColor[currentPosition] = tocolor
    for togo in edges[currentPosition]:
        if togo in notvisited:
            dfs(notvisited,togo,edges, tocolor, nodeColor)

def colorBlueToFindCycle(nodeColor, fromcolor, tocolor):
    for idx, i in enumerate(nodeColor):
        if i == fromcolor:
            nodeColor[idx] = tocolor


n, m, k = map(int, input().split()) 
while not n==m==k==0:
    rededges = [[] for _ in range(n)]
    blueedges = [[] for _ in range(n)]
    nodeColor = [-1 for _ in range(n)]
    nodeColorToFindBlueCycle = list(range(n))
    totalBlueEdges = 0
    for _ in range(m):
        inputraw = input().split()
        st = int(inputraw[1])-1
        ed = int(inputraw[2])-1
        if inputraw[0] == 'B':
            if nodeColorToFindBlueCycle[st] == nodeColorToFindBlueCycle[ed]:
                continue
            blueedges[st].append(ed)
            blueedges[ed].append(st)
            colorBlueToFindCycle(nodeColorToFindBlueCycle, nodeColorToFindBlueCycle[st], nodeColorToFindBlueCycle[ed] )
            totalBlueEdges +=1
        else:
            rededges[st].append(ed)
            rededges[ed].append(st)

    currentColor = 0
    notvisited = set(range(n))
    while notvisited:
        for cursor in notvisited:
            break
        dfs(notvisited, cursor, rededges, currentColor, nodeColor)
        currentColor+=1
    #print(nodeColor)

    ingyeo = 0
    blueedgesFinal = [[False for _ in range(currentColor)] for _ in range(currentColor)]
    nodeColorToFindFinalCycle = list(range(currentColor)) 
    effectiveEdges = 0
    #print(blueedges)
    for st, edges in enumerate(blueedges):
        for ed in edges:
            if st <= ed:
                if blueedgesFinal[nodeColor[st]][nodeColor[ed]]:
                    ingyeo+=1
                elif nodeColor[st] == nodeColor[ed]:
                    ingyeo +=1
                elif nodeColorToFindFinalCycle[nodeColor[st]] != nodeColorToFindFinalCycle[nodeColor[ed]]:
                    blueedgesFinal[nodeColor[st]][nodeColor[ed]] = True
                    blueedgesFinal[nodeColor[ed]][nodeColor[st]] = True
                    colorBlueToFindCycle(nodeColorToFindFinalCycle, nodeColorToFindFinalCycle[nodeColor[st]], nodeColorToFindFinalCycle[nodeColor[ed]])
                    effectiveEdges+=1
    assert ingyeo+effectiveEdges == totalBlueEdges
    #print(effectiveEdges, ingyeo, totalBlueEdges)
    if effectiveEdges != currentColor-1:
        print(0)
    else:
        if effectiveEdges <= k <=effectiveEdges+ingyeo:
            print(1)
        else:
            print(0)



    n, m, k = map(int, input().split()) 
