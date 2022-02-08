t = int(input())

def getres():
    dp = dict()
    def finddp(i):
        if i in dp.keys():
            return dp[i]
        return 0
    n = int(input())
    fst = list(map(int, input().split()))
    snd = list(map(int, input().split()))
    for i in range(n):
        dp[(i,0)] = max(finddp((i-1, 0)),finddp((i-1,1)), finddp((i-1,10)))
        dp[(i,1)] = fst[i] + max(finddp((i-1,10)), finddp((i-1,0)))
        dp[(i,10)] = snd[i] + max(finddp((i-1,1)), finddp((i-1,0)))
    print(max(dp[(n-1,0)],dp[(n-1,1)],dp[(n-1,10)]))

for _ in range(t):
    getres()