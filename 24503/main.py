import math
import bisect

import math
def isPrime(n):
    if n<2:
        return False
    s = 0
    area = n
    area-=1
    while(area%2==0):
        s+=1
        area//=2
    a = [2,3,5,7,11,13,17,19,23,29,31,37]
    isp = 0
    for i in a:
        if i >= n:
            isp+=1
            continue
        if (pow(i,area,n)==1):
            isp+=1
            continue
        for r in range(s):
            if pow(i,(2**r)*area,n)==n-1:
                isp+=1
                break
    
    if isp ==len(a):
        return True
    else:
        return False

primes = set()

def pollardrho(ans,todo, n,x0=-1):
    #print(n)
    if isPrime(n):
        ans.add(n)
        return
    if n==4:
        s = (2+x0)**2+x0
        t = (2+x0)
    else:
        s = (3+x0)**2+x0
        t = 3+x0
    s%=n
    t%=n
    g = math.gcd(abs(s-t),n)
    while g==1:
        s = (s**2+x0)%n
        s = (s**2+x0)%n
        t = (t**2+x0)%n
        g = math.gcd(abs(s-t),n)
    #print(g, n ,g==n)
    if g==n:
        if x0==-1:
            todo.append((n,1))
        elif x0==1:
            todo.append((n,2))
        else:
            todo.append((n,(x0+1)%n))
        return
    assert n%g==0
    a= n//g
    todo.append((a,1))
    todo.append((g,1))
    return
chamgo = [1,3,6,10,15,21,28,36,45,55,65]


def rep(a,b):
    cur = b
    while a%b==0:
        tmp = cur
        while tmp%b==0 and a%b==0:
            #print(a,b,tmp)
            tmp//=b
            a//=b
        cur+=b
    #print(cur-b,a, b)
    return (cur-b, a)


k, q = map(int, input().split())
a = map(int, input().split())
ansdict = dict()
anss = []
todo = [(k,1)]
while todo:
    newtodo = []
    for i in todo:
        pollardrho(primes,newtodo,i[0],i[1])
    todo = newtodo
    #print(todo)
    
primes = list(primes)
primes.sort()


#print(primes)
for i in a:
    nk = k//math.gcd(i,k)
    ans = 1
    if nk in ansdict:
        anss.append(ansdict[nk])
        continue
    for prime in primes:
        if nk == 1:
            break
        if nk%prime==0:
            tmp = rep(nk, prime)
            ans = max(ans, tmp[0])
            nk = tmp[1]
    ansdict[nk] = ans
    anss.append(ans)
print(' '.join(map(str, anss)))
