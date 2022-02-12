dp = dict()

n = int(input())

heights = list(map(int, input().split()))

sh = [0]

for i in heights:
    sh.append(sh[-1] + i)
sh.pop(0)


maxdiff = sum(heights)//2

def findh(j,hd):
    if (j,hd) in dp.keys():
        return dp[(j,hd)]
    if hd > sh[j]:
        dp[(j,hd)] = -987654321
        return -987654321
    if hd > maxdiff:
        dp[(j,hd)] = -987654321
        return -987654321
    if j==0:
        if hd == heights[0]:
            return heights[0]
        else:
            dp[(j,hd)] = -987654321
            return -987654321
    curblock = heights[j]
    a = findh(j-1,hd)
    b = findh(j-1,hd+curblock)
    if hd >= curblock:
        c = findh(j-1,hd-curblock)+curblock
    else:
        c = findh(j-1,curblock-hd)+hd

    dp[(j,hd)] = max(a,b,c)
    return dp[(j,hd)]

ans = findh(n-1,0)
if ans >= 0:
    print(ans)
else:
    print(-1)