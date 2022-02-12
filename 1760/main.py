from re import L


n,m= map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

xhubo = [] # horizontal, (y,xs, xe)
yhubo = [] # vertical, (x,ys,ye)
conn = dict()

for idx,line in enumerate(board):
    bef = 2
    start = 0
    end = 0
    for idx2, j in enumerate(line):
        if j!=bef:
            if j == 2:
                end = idx2-1
                xhubo.append((idx,start,end))
            elif bef == 2:
                start = idx2
        bef = j
    if bef < 2:
        end = m-1
        xhubo.append((idx,start,end))

ynum = 0
for idx in range(m):
    bef = 2
    start = 0
    end = 0
    for idx2 in range(n):
        if board[idx2][idx] == 0:
            for xidx, j in enumerate(xhubo):
                if idx2 == j[0] and idx <= j[2] and idx >= j[1]:
                    if xidx in conn.keys():
                        conn[xidx].append(ynum)
                    else:
                        conn[xidx] = [ynum]
        if board[idx2][idx]!=bef:
            if  board[idx2][idx] == 2:
                end = idx2-1
                yhubo.append((idx,start,end))
                ynum+=1
            elif bef == 2:
                start = idx2
        bef =  board[idx2][idx]
    if bef < 2:
        end = n-1
        yhubo.append((idx,start,end))
        ynum+=1

def dfs(i, Ms, visited, current):
    if visited[i] == True:
        return False
    visited[i] = True
    if not i in Ms.keys():
        return False
    for j in Ms[i]:
        if not current[j]>=0 or dfs(current[j],Ms,visited,current):
            current[j] = i
            return True
    return False

current = [-1 for _ in range(len(yhubo))]
for i in range(len(xhubo)):
    visited = [False for _ in range(len(xhubo))]
    dfs(i, conn, visited,current)
print(sum([1 for i in current if i >= 0]))