import math

t=int(input())

def getsize(combi):
    global points
    startx = 0
    starty = 0
    endx = 0
    endy = 0
    for idx, i in enumerate(combi):
        if i == 0:
            endx += points[idx][0]
            endy += points[idx][1]
        else:
            startx += points[idx][0]
            starty += points[idx][1]
    return math.sqrt((endx-startx)**2+(endy-starty)**2)
            




def createcomb(n, cur):
    if sum(cur) < len(cur)-n//2:
        return 
    if sum(cur) >= n//2:
        while len(cur)<n:
            cur.append(0)
    if len(cur) >=n:
        global ans
        ans.append(getsize(cur))
        return
    cur2 = cur[:]
    cur.append(0)
    cur2.append(1)
    createcomb(n,cur)
    createcomb(n,cur2)

for _ in range(t):
    n = int(input()) 
    points = []
    ans = []
    for _ in range(n):
        a,b = map(int, input().split())
        points.append((a,b))
    createcomb(n,[])
    print(min(ans))
