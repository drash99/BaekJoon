n, k = map(int, input().split())
a = list(map(int, input().split()))

a = a[:]+a[:]
ans = sum(a[0:k])
maxi = ans
for i in range(1,n):
    ans -= a[i-1]
    ans += a[i+k-1]
    maxi = max(maxi,ans)

print(maxi)