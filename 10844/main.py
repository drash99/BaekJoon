N = int(input())

dp = dict()
dp[(1,0)] = 0
for i in range(1,10):
    dp[(1,i)] = 1

for i in range(2,101):
    dp[(i,0)] = dp[(i-1,1)]
    dp[(i,9)] = dp[(i-1,8)]
    for j in range(1,9):
        dp[(i,j)] = dp[(i-1,j-1)]+dp[(i-1),(j+1)]

ans = 0
for i in range(10):
    ans += dp[(N,i)]
    
print(ans%1000000000)
