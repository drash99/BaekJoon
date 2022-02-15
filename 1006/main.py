t = int(input())
inf = 987654321


def calcdp(dp,n, start=1, offset = 0):
    for i in range(start,n+1):
        if field[0][i-1] +field[1][i-1] <= w:
            dp[i][0] = dp[i-1][0]+1
        dp[i][0] = min(dp[i][0], dp[i-1][1]+1,dp[i-1][2]+1, dp[i-1][0]+2, dp[i-1][3])
        if field[0][i] + field[0][i-1] <= w:
            dp[i][2] = dp[i-1][1]+1
            if field[1][i] + field[1][i-1] <= w:
                dp[i][1] = dp[i-1][2]+1
                dp[i][3] = dp[i-1][0]+2
            dp[i][1] = min(dp[i][1], dp[i][0]+1)
        else:
            if field[1][i] + field[1][i-1] <= w:
                dp[i][1] = dp[i-1][2]+1
            dp[i][1] = min(dp[i][1], dp[i][0]+1)
        dp[i][2] = min(dp[i][2], dp[i][0]+1)

    #print(n,start, offset, dp[0:n-offset+1])
    return dp[n-offset]

for _ in range(t):
    n,w = map(int, input().split())
    field = []
    field.append(list(map(int, input().split())))
    field.append(list(map(int, input().split())))
    field[0].append(field[0][0])
    field[1].append(field[1][0])

    
    firstcon = False
    secondcon = False
    if field[0][-1] + field[0][-2] <= w:
        firstcon = True
    if field[1][-1] + field[1][-2] <= w:
        secondcon = True
    dp = [[inf,inf,inf,inf] for _ in range(10001)] ## 00 01 10 11
    dp[0][0] = 0
    dp[0][1] = 1
    dp[0][2] = 1    

    ans = calcdp(dp,n)[0]

    #print(ans)
    if firstcon :
        dp = [[inf,inf,inf,inf] for _ in range(10001)] ## 00 01 10 11
        dp[1][0] = 2
        dp[1][1] = 2 if field[1][0] + field[1][1] <= w else 3
        dp[1][2] = 3    
        ans = min(ans, calcdp(dp,n,2,1)[1])
    
    if secondcon :
        dp = [[inf,inf,inf,inf] for _ in range(10001)] ## 00 01 10 11
        dp[1][0] = 2
        dp[1][2] = 2 if field[0][0] + field[0][1] <= w else 3
        dp[1][1] = 3    
        ans = min(ans, calcdp(dp,n,2,1)[2])
    
    if secondcon and firstcon:
        dp = [[inf,inf,inf,inf] for _ in range(10001)] ## 00 01 10 11
        dp[1][0] = 2
        dp[1][1] = 3
        dp[1][2] = 3    
        ans = min(ans, calcdp(dp,n,2,1)[0])

    print(ans)
        
        

