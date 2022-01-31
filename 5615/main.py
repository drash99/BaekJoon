

def isPrime(area):
    s = 1
    n = area*2+1
    while(area%2==0):
        s+=1
        area = area//2

    #print(area,s,n)
    a = [2,7,61]
    isp = 0
    for i in a:
        if i >= n:
            isp+=1
            continue
        if (pow(i,area,n)==1):
            isp+=1
            continue
        for r in range(s):
            if pow(i,(2**r)*area,n)==n-1:
                isp+=1
                continue
    
    if isp ==3:
        return 1
    else:
        return 0

def ispossible(ans, area):
    if area<4:
        ans[0] += 1
        return
    ans[0] += isPrime(area)

N = int(input().strip())
ans = [0]

for i in range(N):
    a = int(input())
    ispossible(ans,a)
print(ans[0])
