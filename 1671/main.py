n = int(input())

abil = []
single = set()
for i in range(n):
    abil.append(tuple(map(int,input().split())))

def compabil(idxa, idxb):
    a = abil[idxa]
    b = abil[idxb]
    if a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2]:
        if a[0] == b[0] and a[1] == b[1] and a[2] == b[2]:
            if (idxb, idxa) in single:
                return False
            single.add((idxa,idxb))
        return True
    return False
def dfs(i, abil, visited, current):
    if visited[i] == True:
        return False
    visited[i] = True

    
    for idx,j in enumerate(abil):
        if idx != i//2 and compabil(i//2, idx):
            if not current[idx]>=0 or dfs(current[idx],abil,visited,current):
                current[idx] = i
                return True
    return False
    

current = [-1 for _ in range(n)]
for i in range(n*2):
    visited = [False for _ in range(n*2)]
    dfs(i, abil, visited,current)
print(n-sum([1 for i in current if i >= 0]))
    
                