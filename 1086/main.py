import math
n = int(input())

nfac =1 
for i in range(2,n+1):
    nfac*=i

a = []
lena = []

for _ in range(n):
    tmp = int(input())
    tmpl = len(str(tmp))
    a.append(tmp)
    lena.append(tmpl)
    

k = int(input())

dp = [[0 for _ in range(k)] for _ in range(2**n)]
dpdec = []
tmp = 1
for _ in range(760):
    dpdec.append(tmp)
    tmp*=10
    tmp%=k

def calclen(bitmask):
    tmp = bitmask
    fromright = 0
    ans = 0
    while tmp>=1:
        if tmp%2==1:
            ans+=lena[fromright]
        fromright+=1
        tmp//=2
    return ans

dp[0][0] = 1
for i in range(1,2**n):
    tmp = i
    fromright = 0
    while tmp >= 1:
        tmp//=2
        fromright +=1
    #print(i,fromright)
    for l in range(fromright):
        if 2**l & i == 0:
            continue
        tmp = i^(2**l)
        ne = a[l]
        nel = lena[l]
        tmpl = calclen(tmp)
        #print(tmp, nel, ne, tmpl)
        #print(tmpl)
        for j in range(k):
            dp[i][(j+ne*dpdec[tmpl])%k] += dp[tmp][j]

#print(dp)
bunja = dp[(2**n)-1][0]
bunmo = nfac
g = math.gcd(bunja, bunmo)
bunja//=g
bunmo//=g
print(f"{bunja}/{bunmo}")



