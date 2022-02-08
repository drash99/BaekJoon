n = int(input())
dp = dict()
def finddp(i):
    if i in dp.keys():
        return dp[i]

    return 0

data = []
for i in range(n):
    data.append(tuple(map(int, input().split())))

def calcdp(fst):

    dp[(1,0)] = 1000000
    dp[(1,1)] = 1000000
    dp[(1,2)] = 1000000
    
    dp[(1,fst)] = data[0][fst]

    for i in range(2, n+1):
        dp[(i,0)] = min(finddp((i-1,1)),finddp((i-1,2)))+data[i-1][0]
        dp[(i,1)] = min(finddp((i-1,0)),finddp((i-1,2)))+data[i-1][1]
        dp[(i,2)] = min(finddp((i-1,1)) , finddp((i-1,0)))+data[i-1][2]
    return min(finddp((n,(fst-1)%3)),finddp((n,(fst-2)%3)))



print(min(calcdp(0),calcdp(1),calcdp(2)))