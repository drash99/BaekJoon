import math
n,m = map(int,input().split())

field = []
for _ in range(n):
    field.append(list(map(int, list(input()))))


ans = []

for i in range(n):
    for j in range(m):
        for x in range(n):
            for y in range(m):
                if i==x and j==y:
                    h = field[i][j]
                    if math.sqrt(h).is_integer():
                        ans.append(h)
                    continue
                hubo = [field[i][j]]
                cursorx = x
                cursory = y
                current = field[i][j]
                while cursorx <n and cursory <m and cursorx>=0 and cursory >=0:
                    current *=10
                    #print(cursorx,cursory)
                    current +=field[cursorx][cursory]
                    cursorx+=x-i
                    cursory+=y-j
                    hubo.append(current)
                for h in hubo:
                    if math.sqrt(h).is_integer():
                        ans.append(h)

if ans:
    print(max(ans))
else:
    print(-1)