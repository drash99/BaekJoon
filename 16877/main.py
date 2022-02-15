fibs = [1,2,3,5,8,13]
while(fibs[-1]+fibs[-2] < 3000000):
    fibs.append(fibs[-1]+fibs[-2])

ans = [0 for _ in range(3000001)]

cur = 0
for i in range(0,3000001):
    shown = set()
    for j in fibs:
        if i-j >=0:
            shown.add(ans[i-j])
        else:
            break
    for j in range(3000000):
        if not j in shown:
            ans[i] = j
            break

n = int(input())
p = list(map(int, input().split()))
answ = ans[p[0]]
for i in range(1,n):
    answ ^= ans[p[i]]
print('koosaga' if answ!=0 else 'cubelover')