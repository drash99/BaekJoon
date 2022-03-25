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

def multiply(a:list, b:list) -> list:
    n=1
    while (n < len(a)+1 or n < len(b)+1):
        n*=2
    n*=2
    while len(a)<n:
        a.append(0)
    while len(b)<n:
        b.append(0)
    c = [0 for _ in range(n)]

    w = complex(math.cos(2*math.pi/n),math.sin(2*math.pi/n))
    
    FFT(a,w)
    FFT(b,w)

    for i in range(n):
        c[i] = a[i]*b[i]
    
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


a = [0]*140000
b = [0]*140000
c = [0]*140000
n = int(input())
for k in map(int, input().split()):
    a[k+30000] = 1

n = int(input())
for k in map(int, input().split()):
    b[k+30000] = 1

n = int(input())
for k in map(int, input().split()):
    c[k+30000] = 1

print(a[29990:30010])
print(c[29990:30010])
res =multiply(a,c)
print(res[59990:60010])
ans = 0
for idx,i in enumerate(b):
    if i and res[idx*2].real:
        ans+=round(res[idx*2].real)

print(ans)