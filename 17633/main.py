import math
from random import randint

def isPrime(n):
    if n==2: return True
    if n<2 or n%2==0:
        return False
    s = 0
    area = n
    area-=1
    while(area&1):
        s+=1
        area>>=1
    a = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    isp = 0
    for i in a:
        if i >= n:
            isp+=1
            continue
        if (pow(i,area,n)==1):
            isp+=1
            continue
        for r in range(s):
            if pow(i,area>>r,n)==n-1:
                isp+=1
                break
    
    if isp ==len(a):
        return True
    else:
        return False

ans = dict()

def pollardrho(ans,todo, n):
    #print(n,x0)
    if n==1: return
    if n%2==0:
        if 2 in ans:
            ans[2]+=1
        else:
            ans[2]=1
        todo.append(n//2)
        return
        
    if isPrime(n):
        if n in ans:
            ans[n]+=1
        else:
            ans[n]=1
        return
    x0 = randint(1,n-1)
    c = randint(2,n-1)
    s = (c+x0)**2+x0
    t = (c+x0)
    s%=n
    t%=n
    #print(s,t, x0)
    g = math.gcd(abs(s-t),n)
    while g==1:
        s = (s**2+x0)%n
        s = (s**2+x0)%n
        t = (t**2+x0)%n
        g = math.gcd(abs(s-t),n)
    #print(g, n ,g==n)
    if g==n:
        todo.append(n)
        return
    assert n%g==0
    a= n//g
    todo.append(a)
    todo.append(g)
    return

n = int(input())

todo = [n]
while todo:
    newtodo = []
    for i in todo:
        pollardrho(ans,newtodo,i)
    todo = newtodo
    #print(todo)

fac = ans
#print(fac)


def check1(fac):
    for i in fac:
        if fac[i]%2!=0:
            return False
    return True

def check2(fac):
    for i in fac:
        if i%4 == 3 and fac[i]%2==1:
            return False
    return True

def check3(fac,n):
    if not 2 in fac:
        if n%8 ==7:
            return False
    if (2 in fac and fac[2]%2==0):
        if (n//(2**fac[2]))%8 ==7:
            return False
    return True


if check1(fac):
    print(1)
elif check2(fac):
    print(2)
elif check3(fac,n):
    print(3)
else:
    print(4)