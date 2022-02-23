import math
import bisect

MAX_SIZE = 40000001
 
# isPrime[] : isPrime[i] is true if
#             number is prime
# prime[] : stores all prime number
#           less than N
# SPF[] that store smallest prime
# factor of number [for ex : smallest
# prime factor of '8' and '16'
# is '2' so we put SPF[8] = 2 ,
# SPF[16] = 2 ]
isprime = [True] * MAX_SIZE
primes = []
SPF = [None] * (MAX_SIZE)
 

# function generate all primes number
# less then N in O(n)
def manipulated_seive(N):
    isprime[0] = isprime[1] = False
    for i in range(2, N):
        # If isPrime[i] == True then i is
        # prime number
        if isprime[i] == True:
            primes.append(i)
            # A prime number is its own smallest
            # prime factor
            SPF[i] = i
        # Remove all multiples of i*prime[j]
        # which are not prime by making is
        # Prime[i * prime[j]] = false and put
        # smallest prime factor of i*Prime[j]
        # as prime[j] [ for exp :let i = 5 , j = 0 ,
        # prime[j] = 2 [ i*prime[j] = 10 ]
        # so smallest prime factor of '10' is '2'
        # that is prime[j] ] this loop run only one
        # time for number which are not prime
        j = 0
        while (j < len(primes) and
               i * primes[j] < N and
                   primes[j] <= SPF[i]):
         
            isprime[i * primes[j]] = False
 
            # put smallest prime factor of i*prime[j]
            SPF[i * primes[j]] = primes[j]
             
            j += 1
         

manipulated_seive(40000000)
chamgo = [1,3,6,10,15,21,28,36,45,55,65]


def rep(a,b):
    ans = 0
    while a%b==0:
        ans+=1
        a//=b
    return (bisect.bisect_left(chamgo, ans)+1, a)
    

k, q = map(int, input().split())
a = map(int, input().split())
ansdict = dict()
anss = []
primenew =[]
#print(primes[:10])
for prime in primes:
    if prime > k:
        break
    if k%prime ==0:
        primenew.append(prime)
primes = primenew

#print(primes)
for i in a:
    nk = k//math.gcd(i,k)
    ans = 0
    if nk in ansdict:
        anss.append(ans)
        continue
    for prime in primes:
        if nk == 1:
            break
        if nk%prime==0:
            tmp = rep(nk, prime)
            ans = max(ans, prime*tmp[0])
            nk = tmp[1]
    ansdict[nk] = ans
    anss.append(ans)
print(' '.join(map(str, anss)))
