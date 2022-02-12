n, b,c = map(int, input().split())

t = b+2*c
tw = b+c

price = 0

a = list(map(int, input().split()))

ones = 0
twos = 0
threes = 0
onenxt = 0
twonxt = 0
threenxt = 0

if b > c:
    for i in range(n):
        price += t*threes
        if a[i] >= ones:
            twonxt = ones
            a[i] -= ones
            ones = 0
        else:
            twonxt = a[i]
            price += b*(ones-a[i])
            a[i] = 0


        if a[i] >= twos:
            print(twos)
            threenxt = twos
            a[i] -= twos
            twos = 0
        else:
            threenxt = a[i]
            price += tw*(twos-a[i])
            a[i] = 0   
        ones = a[i]
        twos = twonxt
        threes = threenxt
    print(price+t*threes+tw*twos+b*ones)
else:
    print(sum(a)*b)
