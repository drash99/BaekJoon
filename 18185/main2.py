n = int(input())

price = 0

a = list(map(int, input().split()))

ones = 0
twos = 0
threes = 0
onenxt = 0
twonxt = 0
threenxt = 0
for i in range(n):
    price += 7*threes
    if a[i] >= ones:
        twonxt = ones
        a[i] -= ones
        ones = 0
    else:
        twonxt = a[i]
        price += 3*(ones-a[i])
        a[i] = 0

    
    if a[i] >= twos:
        print(twos)
        threenxt = twos
        a[i] -= twos
        twos = 0
    else:
        threenxt = a[i]
        price += 5*(twos-a[i])
        a[i] = 0   
    ones = a[i]
    twos = twonxt
    threes = threenxt

print(price+7*threes+5*twos+3*ones)