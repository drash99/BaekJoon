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

ans = []

def pollardrho(ans,todo, n,x0=-1):
    #print(n,x0)
    if isPrime(n):
        ans.append(n)
        return
    if n==4:
        s = (2+x0**2)**2+x0
        t = (2+x0**2)
    else:
        s = (3+x0)**2+x0
        t = 3+x0
    s%=n
    t%=n
    print(s,t, x0)
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

n = int(input())

todo = [(n,1)]
while todo:
    newtodo = []
    for i in todo:
        pollardrho(ans,newtodo,i[0],i[1])
    todo = newtodo
    #print(todo)
    
ans.sort()
for a in ans:
    print(a)
