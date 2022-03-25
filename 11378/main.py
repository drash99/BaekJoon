N, M, k  = map(int, input().split(' '))

Ms = [[] for _ in range(N)]

for i in range(N):
    for j in input().split(' ')[1:]:
        Ms[i].append(int(j)-1)

def dfs(i, Ms, visited, current):
    if visited[i] == True:
        return False
    visited[i] = True
    
    for j in Ms[i]:
        if not current[j]>=0 or dfs(current[j],Ms,visited,current):
            current[j] = i
            return True
    return False
    
current = [-1 for _ in range(M)]
for i in range(N):
    visited = [False for _ in range(N)]
    dfs(i, Ms, visited,current)
ans1 = sum([1 for i in current if i >= 0])
start = ans1

for i in range(N):
    visited = [False for _ in range(N)]
    dfs(i, Ms, visited,current)
ans2 =sum([1 for i in current if i >= 0]) 

while ans2 - start <= k and ans2 != ans1:
    print(start, ans1, ans2)
    tmp = ans1
    ans1 = ans2
    for i in range(N):
        visited = [False for _ in range(N)]
        dfs(i, Ms, visited,current)
    ans2 =sum([1 for i in current if i >= 0]) 

print(current)

if ans2-start > k:
    print(start+k)
else:
    print(ans2)    
                