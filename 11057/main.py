n = int(input())

dp = dict()

for i in range(10):
    dp[(1,i)] = 1

for i in range(2,n+1):
    for j in range(10):
        dp[(i,j)] = 0
        for k in range(0,j+1):
            dp[(i,j)] += dp[(i-1,k)]

ans = 0
for i in range(10):
    ans += dp[(n,i)]

print(ans%10007)
