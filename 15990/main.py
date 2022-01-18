import sys
sys.setrecursionlimit(10**6)
ans = dict()
ans[(3,3)] = 1
ans[(3,2)] = 1
ans[(3,1)] = 1
ans[(2,3)] = 0
ans[(2,2)] = 1
ans[(2,1)] = 0
ans[(1,3)] = 0
ans[(1,2)] = 0
ans[(1,1)] = 1


T = int(input())

def find(num, last):
    if (num,last) in ans.keys():
        return ans[(num,last)]
    tmp1 = find(num-last, ((last%3)+1))+find(num-last, ((last+1)%3+1))
    ans[(num,last)] = tmp1%1000000009
    return tmp1%1000000009

for i in range(1,100000):
    find(i,1)
    find(i,2)
    find(i,3)

for i in range(T):
    N = int(input())
    print((find(N,1)+find(N,2)+find(N,3))%1000000009)
