inputraw = input().strip().split(' ')
N = int(inputraw[0])
M = int(inputraw[1])
P = int(inputraw[2])
modu = 1000000007

def fac(num):
    ans = 1
    for i in range(1,num+1):
        ans *= i
        ans %= modu
    return ans

