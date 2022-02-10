t,a,s,b = map(int, input().split())

nums = [0 for _ in range(t+1)]
def putnum(i):
    nums[int(i)]+=1

inraw = map(int, input().split())
for i in inraw:
    putnum(i)

dp = [[0 for _ in range(a+1)] for _ in range(t+1)]
dp[0][0] = 1
size = 0
for i in range(1,t+1):
    if nums[i]==0:
        for j in range(a+1):
            dp[i][j] = dp[i-1][j]
    else:
        for j in range(a+1):
            for k in range(nums[i]+1):
                dp[i][j] += dp[i-1][j-k]


    
ans = 0
for i in range(s, b+1):
    ans += dp[t][i]
print(ans%1000000)