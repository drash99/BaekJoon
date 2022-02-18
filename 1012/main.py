import sys
input = sys.stdin.readline

def dfs(field,bachu, pos, n, m):
    if not pos in bachu:
        return
    bachu.remove(pos)
    x,y = pos
    if x>0 and field[x-1][y] == 1:
        dfs(field, bachu, (x-1,y), n,m)
    if x<m-1 and field[x+1][y] == 1:
        dfs(field, bachu, (x+1,y), n,m)
    if y>0 and field[x][y-1] == 1:
        dfs(field, bachu, (x,y-1), n,m)
    if y<n-1 and field[x][y+1] == 1:
        dfs(field, bachu, (x,y+1), n,m)

        


for _ in range(int(input())):
    m,n,k = map(int,input().split())
    field = [[0 for _ in range(n)] for _ in range(m)]
    bachu = set()
    for _ in range(k):
        x, y = map(int,input().split())
        bachu.add((x,y))
        field[x][y] = 1
    ans = 0
    while bachu:
        e = bachu.pop()
        bachu.add(e)
        dfs(field,bachu, e, n, m)
        ans+=1
    print(ans)
    
