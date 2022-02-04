primes = [2]

ispossible = True
for i in range(3,2001,2):
    ispossible = True
    for prime in primes:
        if i%prime == 0:
            ispossible =False
            break
    if ispossible:
        primes.append(i)

odds = []
evens = []

input()
dataraw = input().split(' ')

first = int(dataraw[0])

for datum in dataraw:
    tmp = int(datum)
    if tmp%2 == 0:
        evens.append(tmp)
    else:
        odds.append(tmp)


def dfs(i, odds, evens, visited, current):
    if visited[i] == True:
        return False
    visited[i] = True

    for j in range(len(evens)):
        if odds[i]+evens[j] in primes:
            if not current[j]>=0 or dfs(current[j],odds,evens,visited,current):
                current[j] = i
                return True
    return False
    


def findway(odds, evens):
    current = [-1 for _ in range(len(evens))]
    for i in range(len(odds)):
        visited = [False for _ in range(len(odds))]
        dfs(i, odds, evens, visited,current)
    if sum([1 for i in current if i >= 0]) == len(current):
        return True
    else:
        return False
                


ans = []
isValid = True

if(len(odds)!= len(evens)):
    print(-1)
    isValid = False


if isValid:
    if first %2 == 0:
        for i in odds:
            if i+first in primes:
                oddstmp = odds[:]
                evenstmp = evens[1:]
                oddstmp.remove(i)
                if findway(oddstmp, evenstmp):
                    ans.append(i)
    else:
        for i in evens:
            if i+first in primes:
                oddstmp = odds[1:]
                evenstmp = evens[:]
                evenstmp.remove(i)
                if findway(oddstmp, evenstmp):
                    ans.append(i)
            
    if len(ans) >0:
        print(' '.join(map(str, sorted(ans))))
    else:
        print(-1)


