n = int(input())
a = list(map(int, input().split()))

ans = max(a)
for idx in range(1, len(a)-1):
    tmp = min(a[idx-1], a[idx+1])+a[idx]
    ans = max(tmp,ans)

print(ans)