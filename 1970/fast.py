n = int(input())

hyuns = []

dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

brands = list(map(int, input().split()))
newbrands = []

ans=0
for idx in range(len(brands)):
    if len(newbrands) > 0 and brands[idx]==newbrands[-1]:
        ans+=1
        newbrands.pop()
        continue
    newbrands.append(brands[idx])
#print(newbrands)
brands = newbrands
n = len(brands)
#print(brands, newbrands)
tmpset = [[] for _ in range(101)]
for idx, i in enumerate(brands):
    for j in tmpset[i]:
        hyuns.append((j, idx+1))
    tmpset[i].append(idx+1)

def solve(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    if len(set(brands[i:j])) == 1:
        return (j-i)//2

    dp[i][j] = 0
    for a,b in hyuns:
        if i == a and j == b: continue
        if i <= a <= b <= j:
            dp[i][j] = max(dp[i][j], solve(i,a) + solve(a,b)+ solve(b, j) + 1)
    return dp[i][j]

print(ans+solve(0,n))
