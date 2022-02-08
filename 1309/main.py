n = int(input())

dp = dict()

def finddp(i):
    if i in dp.keys():
        return i
    return 0

dp[(1,1)] = 2
dp[(1,0)] = 1

for i in range(2, n+1):
    dp[(i,0)] = (dp[(i-1,0)] + dp[(i-1,1)])%9901
    dp[(i,1)] = (2*dp[(i-1,0)] + dp[(i-1,1)])%9901

print((dp[(n,0)]+dp[(n,1)])%9901)