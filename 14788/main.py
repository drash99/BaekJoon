t = int(input())

def findpos(s,k):
    cnt = 0
    for j in range(len(s)-k+1):
        if s[j] == 1:
            for i in range(k):
                s[i+j] +=1
                s[i+j] %=2
            cnt+=1
    if sum(s) == 0:
        return cnt
    else:
        return 90000
            

for i in range(t):
    raw = input().split()
    s = list(map(lambda x: 0 if x=='+' else 1, list(raw[0])))
    k = int(raw[1])
    ans = findpos(s,k)
    if ans <=9000:
        print(f"Case #{i+1}: {ans}")
    else:
        print(f'Case #{i+1}: IMPOSSIBLE')