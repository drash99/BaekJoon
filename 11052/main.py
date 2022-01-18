
ans = dict()
ans[0] = 0
N = int(input())
Praw = input().strip().split(' ')
p = [0]
for ps in Praw:
    p.append(int(ps))

def find(n, arr):
    if n in ans.keys():
        return ans[n]
    maxi = 0
    for i in range(1,n+1):
        tmp = p[i] + find(n-i,arr)
        maxi = max(tmp,maxi)
    ans[n] = maxi
    
    return maxi

print(find(len(p)-1,p))