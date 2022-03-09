import math
import cmath

def FFT(f:list, w:complex) -> None:
    n = len(f)
    if n==1:
        return
    
    even = f[::2]
    odd = f[1::2]

    FFT(even, w*w)
    FFT(odd, w*w)

    wp = 1+0j
    for i in range(n//2):
        f[i] = even[i] + wp*odd[i]
        f[i+n//2] = even[i] - wp*odd[i]
        wp *= w

def multiply(a:list) -> list:
    n=1
    while (n < len(a)+1):
        n*=2
    n*=2
    while len(a)<n:
        a.append(0)
    c = [0 for _ in range(n)]

    w = complex(math.cos(2*math.pi/n),math.sin(2*math.pi/n))
    
    FFT(a,w)

    for i in range(n):
        c[i] = a[i]*a[i]
    
    FFT(c, complex(1,0)/w)
    for i in range(n):
        c[i] /= complex(n,0)
        c[i] = complex(round(c[i].real),round(c[i].imag))
    return c

def compToint(a:list) -> int:
    ans = 0
    for idx, i in enumerate(a):
        #assert i.imag!=0
        ans += i.real*(10**idx)
    return int(ans)



n = int(input())
a = [0]*(n+1)
for i in range(1,n):
    a[(i*i)%n] += 1

c = a[:]

res =multiply(a)

for i in range(n,2*n):
    res[i-n] += res[i]
    res[i] =0
res = res[:n+1]
tmp = [0]*(n+1)
for i in range(n):
    if c[(2*i)%n]:
        tmp[(2*i)%n] += c[i]

#print(res)
tmpans = 0
for i in range(n+1):
    if c[i%n] != 0 and res[i]:
        res[i] -= tmp[i]
        tmpans += tmp[i]*c[i%n]

#print(res)
#print(c)
ans = 0
for idx, i in enumerate(res):
    if c[idx%n] != 0:
        ans += round(i.real)*c[idx%n]
#assert ans%2==0

ans //=2
#print(ans)
ans += tmpans
while True:
    pass
print(ans)