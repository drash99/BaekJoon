N, M = map(int, input().split(' '))

Ms = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    Ms[a-1].append(b-1)

def dfs(i, Ms, visited, current):
    if visited[i] == True:
        return False
    visited[i] = True

    for j in Ms[i]:
        if not current[j]>=0 or dfs(current[j],Ms,visited,current):
            current[j] = i
            return True
    return False
    

current = [-1 for _ in range(N)]
for i in range(N):
    visited = [False for _ in range(N)]
    dfs(i, Ms, visited,current)
print(sum([1 for i in current if i >= 0]))
    
                