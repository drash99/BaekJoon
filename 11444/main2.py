n = int(input())
modu = 1000000007

dp = dict()
dp[2] = 1
dp[1] = 1
dp[0] = 0
def fib(i):
    if i in dp.keys():
        return dp[i]
    if i%2==0:
        ans = (2*fib(i//2+1)-fib(i//2))*fib(i//2)%modu
        dp[i] = ans
        return ans
    else:
        ans = ((fib(i//2+1)%modu)**2+(fib(i//2)%modu)**2)%modu
        dp[i] = ans
        return ans

print(fib(n+n%2))