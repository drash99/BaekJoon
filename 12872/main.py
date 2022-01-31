inputraw = input().strip().split(' ')
N = int(inputraw[0])
M = int(inputraw[1])
P = int(inputraw[2])
modu = 1000000007

def fac(num,start = 1):
    ans = 1
    for i in range(start,num+1):
        ans *= i
        ans %= modu
    return ans

dp = dict() #N, P

dp[(M,M)] = fac(N, N-M+1)

def finddp(key):
    if key in dp.keys():
        return dp[key]
    else:
        return 0

for i in range(M,P):
    for j in range(M, N):
        dp[(i+1,j+1)] = (finddp((i,j+1)) * (j+1-M) + finddp((i,j)) * (N-j))%modu

print(finddp((P,N)))
