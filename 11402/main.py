n,k,m = map(int, input().split())

def moddiv(k,m):
    return pow(k,m-2,m)

def comb(n,k,m):
    ans = 1
    for i in range(k):
        ans *= (n-i)
        ans *= moddiv(i+1,m)
        ans %= m
    return ans

ans = 1
while n//m!=0 and k//m!=0:
    ni = n%m
    ki = k%m
    #print(ni,ki,ans)
    ans *= comb(ni,ki,m)%m
    n //=m
    k//=m

#print(ans, n, k, m)
ans *= comb(n,k,m)%m


print(ans%m)
