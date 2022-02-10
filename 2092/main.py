t,a,s,b = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

streak= 0 
last = 0

dp = dict()
dp[(0,0)] = 1

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

for idx, i in enumerate(nums):
    if i == last:
        streak+=1
        dp[(idx+1,0)] = 1
        for j in range(min(b, idx+1)):
            dp[(idx+1,j+1)] = (finddp((idx, j))-finddp((idx-1,j)))+ finddp((idx,j+1))
            
    else:
        streak = 1
        dp[(idx+1,0)] = 1
        for j in range(min(b, idx+1)):
            dp[(idx+1,j+1)] = finddp((idx, j))+ finddp((idx,j+1))
        last = i

    
ans = 0
for i in range(s, b+1):
    ans += finddp((a, i))
print(ans%1000000)