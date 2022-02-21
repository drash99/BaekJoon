

def gethap(i):
    ans = i
    while i>0:
        ans+=i%10
        i//=10
    return ans
ans = []
for n in range(1, 1000000):
    for j in range(1,10):
        jari = len(str(n))
        i= n-jari*10+j
        if gethap(i) == n:
            ans.append((jari*10+j,i,n))
            break

ans.sort()
print(ans)