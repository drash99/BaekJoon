import bisect

primes = [2]

primehubo = set(range(3,1000000,2))


while primehubo:
    p = primehubo.pop()
    primes.append(p)
    for i in range(p,1000000,p):
        primehubo.discard(i)
    
zegops = list(map(lambda x:x*x, primes))

mi ,ma = map(int,input().split())

st = bisect.bisect_left(zegops,mi)
ed = bisect.bisect_right(zegops,ma)


    
anshubo = set(range(mi, ma+1))
for zegop in zegops:
    for i in range((mi//zegop) * zegop, ma+1, zegop):
        anshubo.discard(i)



print(len(anshubo))