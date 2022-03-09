import math

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
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()
    a.extend([0.0] * (n - len(a)))
    b.extend([0.0] * (n - len(b)))
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

def findMax(a:list) -> int:
    ans = 0
    for i in a:
        ans = max(ans, i.real)
    return int(ans)


n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
y.extend(y)
y.reverse()
c = multiply(x,y)
print(findMax(c))