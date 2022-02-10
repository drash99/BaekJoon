import sys
n, m = map(int, input().split())

table = []

dp = dict()

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

for i in range(n):
    table.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        dp[(i,j)] = finddp((i-1,j))+finddp((i,j-1))-finddp((i-1,j-1))+table[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    print(finddp((x2-1,y2-1))-finddp((x2-1,y1-2))- finddp((x1-2,y2-1))+finddp((x1-2,y1-2)))
