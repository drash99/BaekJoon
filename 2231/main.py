n = int(input())
jari = len(str(n))

def gethap(i):
    ans = i
    while i>0:
        ans+=i%10
        i//=10
    return ans
ans = 0
for i in range(n-jari*10,n):
    if gethap(i) == n:
        ans = i
        break

print(ans)