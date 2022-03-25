n = int(input())

def find(st):
    if st > 100000:
        return False
    ans = [st]
    used= set()
    used.add(st)
    nujuk = st
    for i in range(1,n):
        for j in range(st%2,100001,2):
            if j in used:
                ispossible =False
                continue
            ispossible = True
            for k in range(1,i):
                if ans[i-k]%k != j%k:
                    ispossible =False
                    break
            if ispossible:
                if (nujuk+j)%(i+1)!=0:
                    ispossible = False
                    continue
                ans.append(j)
                used.add(j)
                nujuk+=j
                break
        if not ispossible:
            return find(st+1)
    return ans
        
        
print(find(1))

ans = list(range(1,2*n,2))
print(' '.join(map(str, ans)))