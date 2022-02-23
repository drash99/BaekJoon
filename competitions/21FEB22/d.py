from random import randrange
import sys
input = sys.stdin.readline


n,m = map(int, input().split())
field = []
for _ in range(n):
    field.append(list(input().strip()))





ans = 0
nume = [[0 for _ in range(m)] for _ in range(n)]
numm = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    es= 0
    ms = 0
    for j in range(m):
        if field[i][j] == 'E':
            es+=1
            if i > 0:
                nume[i][j] = nume[i-1][j] + es
            else:
                nume[0][j] = es
        else:
            if i > 0:
                nume[i][j] = nume[i-1][j] + es
            else:
                nume[0][j] = es
for i in range(n-1,-1,-1):
    es= 0
    ms = 0
    for j in range(m-1,-1,-1):
        if field[i][j] == 'M':
            ms+=1
            if i < n-1:
                numm[i][j] = numm[i+1][j] + ms
            else:
                numm[n-1][j] = ms
        else:
            if i < n-1:
                numm[i][j] = numm[i+1][j] + ms
            else:
                numm[n-1][j] = ms

print(nume, numm)

for i in range(n):
    for j in range(m):
        if field[i][j] == 'S':
            ans+=nume[i][j]*numm[i][j]

print(ans%1000000007)