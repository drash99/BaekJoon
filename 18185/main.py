n = int(input())

price = 0

a = list(map(int, input().split()))

for i in range(n-2):
    temp = a[i]
    maxnum = min(a[i],a[i+1],a[i+2])
    if maxnum!=0:
        price += maxnum*7
        a[i] -= maxnum
        a[i+1] -= maxnum
        a[i+2] -= maxnum
    maxnum = min(a[i],a[i+1])
    if maxnum!=0:
        price += maxnum*5
        a[i] -= maxnum
        a[i+1] -= maxnum
    price += a[i]*3
    a[i] = 0
    if a[i+2] < a[i+1]:
        tmp = min(temp, a[i+1]-a[i+2])
        price -= tmp*2
        a[i+2] += tmp
    print(a)

maxnum = min(a[n-2],a[n-1])
if maxnum!=0:
    price += maxnum*5
    a[i] -= maxnum
    a[i+1] -= maxnum

price += sum(a)*3
print(price)