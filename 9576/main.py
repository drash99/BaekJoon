TC = int(input())

def dfs(i, Ms, visited, current):
    if visited[i] == True:
        return False
    visited[i] = True
    for j in range(Ms[i][0],Ms[i][1]+1):
        if not current[j]>=0 or dfs(current[j],Ms,visited,current):
            current[j] = i
            return True
    return False
    
def work():
    N, M = map(int, input().split())
    Ms = []
    for i in range(M):
        Ms.append(tuple(map(int,input().split())))

    current = [-1 for _ in range(N+1)]
    for i in range(M):
        visited = [False for _ in range(M)]
        dfs(i, Ms, visited,current)
    print(sum([1 for i in current if i >= 0]))

for _ in range(TC):
    work()