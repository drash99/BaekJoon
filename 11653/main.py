

primes = [2]

primehubo = set(range(3,4000,2))


while primehubo:
    p = primehubo.pop()
    primes.append(p)
    for i in range(p,4000,p):
        primehubo.discard(i)
    
n = int(input())

ans = []

while n>1:
    ispossible = False
    for i in range(len(primes)):
        if n%primes[i] == 0:
            ans.append(primes[i])
            n//=primes[i]
            ispossible = True
            break
    if not ispossible:
        ans.append(n)
        break

ans.sort()

for i in ans:
    print(i)
