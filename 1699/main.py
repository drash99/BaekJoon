N = int(input())

dp = dict() #key:N, value:number

dp[0] = 0


maxsq = 316

nums = 0
    
while(nums<100000):
    tmp = set(dp.keys())
    for j in tmp:
        for i in range(1,317):
            if j+i*i>100000:
                break
            if not (j+i*i in dp.keys()):
                dp[j+i*i] = dp[j]+1
                nums +=1 
            elif dp[j+i*i] > dp[j] +1:
                dp[j+i*i] = dp[j]+1

print(len(dp.keys()))
print(dp[N])